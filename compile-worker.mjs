/**
 * Compiles RestedXP guides in a dedicated Web Worker.
 * Expensive Polestar WASM operations stay off the main/UI thread.
 * No account data, guide text, or BattleTag is sent to application servers.
 */
const BASE = new URL("./converter/", import.meta.url).href;
const message = (type, extra = {}) => self.postMessage({ type, ...extra });

async function getEngine() {
  message("phase", { text: "Caricamento motore di conversione…" });
  const [engine, addon, zip, wasm] = await Promise.all([
    import(BASE + "src/build.mjs"),
    import(BASE + "src/addon.mjs"),
    import(BASE + "src/zip.mjs"),
    import(BASE + "forge/polestar_convert_wasm.js")
  ]);
  await wasm.default({ module_or_path: BASE + "forge/polestar_convert_wasm_bg.wasm" });
  return { engine, addon, zip, wasm };
}

async function compile({ files, options, includeEntries }) {
  const virt = new Map(files);
  const root = BASE + "polestar-data/";
  const { engine, addon, zip, wasm } = await getEngine();

  message("phase", { text: "Caricamento dati WoW e avvio della conversione…" });
  const response = await fetch(root + "manifest.json");
  if (!response.ok) throw new Error("Dati di gioco non disponibili: HTTP " + response.status);
  const manifest = await response.json();
  if (!Array.isArray(manifest.files) || !manifest.files.length) {
    throw new Error("Dati di gioco non validi o incompleti");
  }

  const allowed = new Set(manifest.files);
  const cache = new Map();
  const readData = async (path) => {
    if (!allowed.has(path)) return null;
    if (!cache.has(path)) {
      cache.set(path, fetch(root + path).then(async (res) => {
        if (!res.ok) throw new Error("Impossibile leggere " + path + ": HTTP " + res.status);
        return await res.text();
      }));
    }
    return await cache.get(path);
  };

  const result = await engine.buildAddons({
    read: async (path) => virt.get(path.toLowerCase()) ?? null,
    paths: [...virt.keys()],
    readData,
    manifest,
    Compiler: wasm.Compiler,
    pack: { id: options.id, title: options.title, author: "WoW XP Helper" },
    opts: { sources: ["rxp"], routes: options.routes },
    locales: [],
    say: (text) => message("log", { text })
  });

  if (result.errors?.length) {
    message("log", { text: "Errori del compilatore: " + result.errors.length });
    for (const e of result.errors.slice(0, 30)) {
      message("log", { text: "  " + (e.file || "?") + " " + (e.line || "") + ": " + (e.message || String(e)) });
    }
    throw new Error("Compilazione interrotta. Controlla i dettagli dell'operazione.");
  }

  const guideCount = result.runs?.rxp?.guides?.length ?? 0;
  if (!guideCount) {
    throw new Error("Conversione terminata senza guide valide. Verifica la cache RestedXP.");
  }

  const dropped = result.dropped ?? [];
  if (dropped.length) {
    message("log", { text: "Guide scartate dal compilatore: " + dropped.length });
    for (const item of dropped.slice(0, 25)) {
      message("log", { text: "  " + (item.slug || "?") + ": " + (item.errors?.[0]?.message || "Non compatibile") });
    }
  }

  message("phase", { text: "Creazione del pacchetto ZIP…" });

  // Decode each output once. ZIP creation may be expensive, so do it in the worker.
  const entries = addon.addonEntries(result.folder, result.files);
  const archive = zip.zip(entries);
  if (!(archive instanceof Uint8Array) || !archive.byteLength) {
    throw new Error("Pacchetto ZIP vuoto o non valido");
  }

  const output = {
    type: "done",
    filename: "PolestarPack_" + options.id + ".zip",
    folder: result.folder,
    buffer: archive.buffer,
    guideCount,
    droppedCount: dropped.length,
    warnings: result.warnings ?? 0,
    entries: includeEntries ? entries : null
  };

  // Transfer the ZIP bytes rather than duplicating them in browser memory.
  self.postMessage(output, [archive.buffer]);
}

self.onmessage = async ({ data }) => {
  if (!data || data.type !== "compile") return;
  try {
    await compile(data);
  } catch (error) {
    message("error", {
      text: error instanceof Error ? error.message : String(error),
      stack: error instanceof Error ? error.stack : ""
    });
  }
};
