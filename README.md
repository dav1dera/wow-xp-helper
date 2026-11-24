# WoW XP Helper

**RestedXP → Polestar con un solo pulsante**, per chi gioca a WoW Forever.

### [Apri WoW XP Helper](https://dav1dera.github.io/wow-xp-helper/)

## Come si usa: tre passaggi, senza istruzioni nascoste

La schermata principale è suddivisa in **tre schede numerate**. Le istruzioni fondamentali sono sempre visibili e ciascun pulsante si trova direttamente nel passaggio a cui appartiene.

1. **Prepara le guide RestedXP.** Se le hai già importate e sono aggiornate, premi **SÌ, LE HO GIÀ → VAI AL PASSAGGIO 2**. Altrimenti segui le istruzioni A, B e C: ottieni un codice dalle fonti a cui hai diritto di accesso, esegui **Purge** soltanto se devi sostituire guide vecchie e hai già il nuovo codice, infine **Import → Reload**. Conferma con la prima casella.
2. **Converti.** Chiudi WoW con **Exit Game** e seleziona la seconda casella. Il **metodo consigliato** ha i due selettori file sempre visibili: scegli `RXPGuides.lua` da `_forever_/WTF/Account/<account>/SavedVariables/` e, per includere le guide iniziali 1–20, la cartella `RXPGuides` da `_forever_/Interface/AddOns/`. Premi **CREA LE GUIDE PER POLESTAR**. Se preferisci, il secondo metodo prova a leggere tutta la cartella `_forever_`, ma Chrome può bloccarla perché contiene file protetti.
3. **Installa.** Quando è pronto, apri lo ZIP scaricato, estrai tutte le cartelle `PolestarPack_*` in `_forever_/Interface/AddOns/`, riavvia WoW e apri **Polestar → Community guides**. La pagina mostra il riepilogo e scorre direttamente alle istruzioni di installazione.

Le azioni di conversione sono disabilitate finché l'utente non conferma che **le guide sono presenti** e che **WoW è chiuso**. I dettagli tecnici e i filtri avanzati rimangono secondari.

**Requisiti:** Chrome o Edge aggiornato su Windows, RestedXP e Polestar già installati. Se manca `RXPGuides.lua`, importa le guide in RestedXP, fai Reload e chiudi completamente il gioco. La conversione resta possibile senza la cartella iniziale, ma in quel caso i primi livelli potrebbero mancare.

Le impostazioni iniziali includono **solo Speedrun**, con due pacchetti Community distinti: **RestedXP Speedrun Horde 1–60** e **RestedXP Speedrun Alliance 1–60**, uno per fazione e senza suddivisioni per livello. **Dungeon e Survival sono facoltativi** nel pannello avanzato e potrebbero generare altri pacchetti. **La copertura effettiva 1–60 non è garantita**: dipende dalle guide realmente presenti nella cache e da quelle accettate dal compilatore.

## Risorse esterne: Inariaa e Forever Free RXP

Inariaa è la prima risorsa esterna elencata nell'interfaccia; Forever Free RXP è la seconda. Sono siti indipendenti e facoltativi. WoW XP Helper non esegue i generatori, non intercetta le loro comunicazioni e non condivide alcun archivio di guide. Le guide ufficiali già importate possono essere utilizzate direttamente.

Forever Free RXP dichiara di basarsi sul [Gist di imSp4rky](https://gist.github.com/imSp4rky/17759ae4bd9a78fdc898c901c2436be1). Quello script non include l'archivio cifrato usato per generare codici nuovi.

## Aggiornamento dalla versione divisa in 14 cartelle

Se hai già provato la vecchia compilazione, **sposta temporaneamente fuori da `Interface/AddOns` le vecchie cartelle `PolestarPack_AllianceSpeedrun*`, `PolestarPack_HordeSpeedrun*` e le vecchie cartelle di Dungeon generate dalla prova**, per evitare duplicati in Polestar. Non toccare gli addon originali `Polestar` e `RXPGuides`.

Il nuovo ZIP contiene **due pacchetti Speedrun separati per fazione** (uno Horde e uno Alliance), ognuno con le proprie tappe collegate da livello 1 a 60, ove disponibili. Può contenere **cartelle addon aggiuntive per razze specifiche** (per esempio `_Human`, `_Gnome`): sono componenti tecnici dello stesso pack, **non pack separati nella schermata Community**; vanno estratti e installati insieme al pack principale.

**Nota sulle prestazioni:** compilare tutte le guide 1–60 di ciascuna fazione in un unico pacchetto richiede più memoria e può impiegare più tempo dei gruppi da 32. Il lavoro avviene in un Web Worker così la pagina resta utilizzabile e offre **Annulla compilazione**. È ancora necessario un test end-to-end con una cache completa dell'utente: il successo di GitHub Actions convalida la pubblicazione, non la compilazione delle sue guide.

## Privacy, licenze e pubblicazione

I file locali vengono elaborati dal browser. **La cache RestedXP e i dati dell'account non vengono caricati da questo progetto.** Il codice del converter e i dati di gioco sono ospitati su GitHub Pages. Quando scegli la cartella WoW, Chrome/Edge deve chiederti il permesso di lettura e scrittura previsto dalle sue protezioni; il tool chiede conferma prima di sostituire una cartella PolestarPack preesistente.

Questo repository non distribuisce guide RestedXP o codici associati ai BattleTag. Usa soltanto guide che hai il diritto di convertire e non distribuire guide di altri senza permesso.

La GUI è rilasciata con licenza MIT. Il motore [polestar-convert](https://github.com/aronjanosch/polestar-convert) è MIT; il compilatore Polestar e i dati utilizzati hanno licenze proprie (incluse GPL-3.0). Gli asset pubblici vengono recuperati durante il workflow GitHub Actions \`.github/workflows/pages.yml\` con \`scripts/vendor_converter.py\`.

Il sito è pubblicato automaticamente su GitHub Pages dopo gli aggiornamenti al ramo \`main\`. La compilazione del sito è verificata da GitHub Actions; la compatibilità con ogni installazione Windows di WoW Forever deve essere verificata sul PC dell'utente.
