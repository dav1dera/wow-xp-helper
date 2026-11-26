# WoW XP Helper

**RestedXP → Polestar con un solo pulsante**, per chi gioca a WoW Forever.

### [Apri WoW XP Helper](https://dav1dera.github.io/wow-xp-helper/)


## Guida rapida: dall'installazione alle guide in Polestar

Apri **[WoW XP Helper](https://dav1dera.github.io/wow-xp-helper/)**. La pagina mostra quattro passaggi, nell'ordine:

1. **Installa WowUp**, da [wowup.io](https://wowup.io/). Seleziona WoW Forever e, in *Get Addons*, installa **RestedXP Guides** e **Polestar Guides**. Se Polestar non compare, usa *Install from URL* con [fitzforge/polestar](https://github.com/fitzforge/polestar). Verifica di usare la versione Forever.
2. **Importa le tue guide in RestedXP**: apri il gioco, *Import Guide*, incolla il codice delle guide che puoi utilizzare, premi *Import* e fai `/reload`. Se erano già importate e aggiornate, salta questo passaggio. Usa **Purge solo per sostituire vecchie guide**, con il codice nuovo già pronto. Chiudi WoW con **Exit Game** per salvare `RXPGuides.lua`.
3. **Converti in Polestar** usando la pagina: seleziona `RXPGuides.lua` e, per includere le guide iniziali, la cartella `RXPGuides`. Il percorso standard precompilato è `C:\Program Files (x86)\World of Warcraft\_forever_`. La pagina offre **Copia percorso** per aprire rapidamente le cartelle dal selettore di file (incolla nella barra indirizzi con `Ctrl+L`, `Ctrl+V`, `Invio`). Se WoW è installato altrove, modifica il percorso sul sito. **Il browser non può aprire direttamente un percorso assoluto senza l'intervento dell'utente.**
4. **Installa e gioca**: estrai le cartelle `PolestarPack_*` dello ZIP direttamente in `_forever_\Interface\AddOns\`. Sposta in un backup i vecchi pacchetti dell'helper per evitare doppioni; non cancellare `Polestar` né `RXPGuides`. Riavvia WoW, usa `/polestar packs` e *Suggest guides from* per attivare la Speedrun. Verifica con `/polestar guides`. Alla schermata personaggi **disabilita RestedXP Guides**, lasciando attivo Polestar. Non disinstallare RestedXP: ti servirà soltanto per aggiornare le guide e rigenerare i pack.

Il risultato predefinito è **una Speedrun 1–60 per Horde e una per Alliance**, nei limiti dei capitoli realmente presenti e convertibili. Dungeon e Survival sono facoltativi. I file delle guide vengono elaborati localmente nel browser.

## Polestar 0.4.3 (25 novembre 2026): compatibilità e aggiornamento

**Le guide Community `PolestarPack_*` prodotte da WoW XP Helper restano supportate:** la 0.4.3 modifica soprattutto il layout dell'addon Polestar, non richiede di cancellare o riconvertire automaticamente i pacchetti delle guide. Il formato Community supporta ancora i pacchetti generati dal compiler ufficiale. Il convertitore incluso nel build recupera a ogni deploy le ultime sorgenti e i dati di `polestar-convert`; il worker passa anche l'elenco dei percorsi sorgente come richiesto dalla versione attuale della libreria.

- **Aggiornamento con gestore addon:** aggiorna `Polestar Guides` tramite il gestore che lo supporta (la release ufficiale suggerisce **CurseForge**). Non effettuare pulizie manuali se il gestore si occupa dell'aggiornamento.
- **Aggiornamento manuale:** esci da WoW, fai un backup e sostituisci le vecchie cartelle dell'addon **Polestar** con quelle di `Polestar-0.4.3.zip` nella cartella `_forever_\Interface\AddOns`. **Non eliminare `PolestarPack_*` né le SavedVariables.** La release passa da 45 a **22 cartelle**; vecchi componenti autonomi come `Polestar_Experimental`, `Polestar_Looks`, `Polestar_SkinAPI`, `Polestar_TabStyles`, `Polestar_Layout_Atlas` e i pacchetti razza separati sono ora accorpati.
- **Primo avvio dopo l'update:** chiudi e riavvia il gioco completamente. **`/reload` non carica le nuove cartelle addon**.
- **Guide installate:** usa `/polestar packs` → *Options → Community guides*, attiva la tua Speedrun Horde/Alliance e scegli *Suggest guides from*. Con `/polestar guides` verifica il risultato. Se il pacchetto segnala errori, apri la sua riga e usa *Show* o *Copy report*.

Fonti: [release Polestar 0.4.3](https://github.com/fitzforge/polestar/releases/tag/v0.4.3), [documentazione Community guides](https://github.com/fitzforge/polestar/blob/v0.4.3/docs/GUIDE_PACKS.md) e [formato dei Community addon](https://github.com/fitzforge/polestar/blob/v0.4.3/docs/PACK_FORMAT.md).

La compilazione e i controlli CI non sostituiscono una prova nel client WoW Forever con una cache `RXPGuides.lua` reale e Polestar 0.4.3.

## Fonti alternative RestedXP e notifiche sugli aggiornamenti

Il passaggio 2 presenta una griglia compatta di **quattro generatori esterni di codici di importazione**, ognuno con un link diretto e un'etichetta consultabile con mouse, tastiera o tocco:

| Fonte | Sito | Che cosa si può verificare |
| --- | --- | --- |
| Inariaa | [rxp_decrypter](https://inariaa.github.io/rxp_decrypter/) | Data del commit GitHub del file inglese `guide.txt`, distinta da aggiornamenti generici del sito |
| Forever Free RXP | [forever-free-rxp.online](https://forever-free-rxp.online/en/) | Versione RestedXP pubblicata e data **Updated** dichiarata sul sito; data effettiva dei file non indipendentemente verificabile |
| Avery Rested Exp | [rested-exp-free](https://averyp-git.github.io/rested-exp-free/) | Ultima modifica del `index.html` del [repository Avery](https://github.com/averyp-git/rested-exp-free): riguarda il sito, **non prova** una nuova versione delle guide |
| Forever RXP | [rxp.kostya.sexy](https://rxp.kostya.sexy/) | Versione RestedXP ed eventuale **data dichiarata dal sito**, esplicitamente distinta da una data verificata sul file sorgente |

Una **notifica toast** compare dopo la verifica delle fonti. Ai controlli successivi segnala se è cambiata la data verificata del file delle guide, una versione dichiarata o soltanto il sito, senza confonderle. Lo stato precedente è salvato soltanto nel browser; puoi chiudere il toast con il pulsante dedicato.

La pagina non indica automaticamente un vincitore se le date delle **guide** non sono confrontabili. Il processo in `scripts/build_guide_sources.py` verifica le fonti durante i deploy e **ogni ora** tramite GitHub Actions, pubblica `guide-sources.json` e include l'ora dell'ultimo controllo (l'esecuzione programmata può subire ritardi su GitHub). **Inariaa è verificata anche direttamente dal browser tramite lo stesso endpoint GitHub usato dal footer ufficiale** (ultimo commit di `guide.txt`), per evitare dati vecchi quando GitHub Actions ritarda. La pagina rilegge i dati ogni **10 minuti** quando è aperta e quando torni alla scheda; il toast segnala solo i cambiamenti rilevati, senza ripetere l'avviso a ogni controllo. Se una fonte non risponde, la pagina conserva l'ultimo valore verificato nel browser e lo etichetta **Ultimo dato**, senza presentarlo come aggiornamento nuovo.

I generatori sono indipendenti da WoW XP Helper, non necessariamente affidabili o completi; alcuni richiedono un BattleTag. Il progetto non inoltra i tuoi dati a queste fonti, non esegue i generatori al tuo posto e non distribuisce archivi di guide.

**RestedXP Cheswick** è stato trovato durante la ricerca ma non inserito nella selezione: durante la verifica automatica il dominio non risultava risolvibile. Sono state trovate anche altre pagine, tra cui **RXP Reforge** (richiede un access code) e **Bulo** (principalmente un tool per adattare file esistenti a un altro BattleTag). Non vengono messe tra i generatori diretti per non appesantire la procedura con strumenti di scopo diverso o con accesso limitato.

## Aggiornamento dalla versione divisa in 14 cartelle

Se hai già provato la vecchia compilazione, **sposta temporaneamente fuori da `Interface/AddOns` le vecchie cartelle `PolestarPack_AllianceSpeedrun*`, `PolestarPack_HordeSpeedrun*` e le vecchie cartelle di Dungeon generate dalla prova**, per evitare duplicati in Polestar. Non toccare gli addon originali `Polestar` e `RXPGuides`.

Il nuovo ZIP contiene **due pacchetti Speedrun separati per fazione** (uno Horde e uno Alliance), ognuno con le proprie tappe collegate da livello 1 a 60, ove disponibili. Può contenere **cartelle addon aggiuntive per razze specifiche** (per esempio `_Human`, `_Gnome`): sono componenti tecnici dello stesso pack, **non pack separati nella schermata Community**; vanno estratti e installati insieme al pack principale.

**Nota sulle prestazioni:** compilare tutte le guide 1–60 di ciascuna fazione in un unico pacchetto richiede più memoria e può impiegare più tempo dei gruppi da 32. Il lavoro avviene in un Web Worker così la pagina resta utilizzabile e offre **Annulla compilazione**. È ancora necessario un test end-to-end con una cache completa dell'utente: il successo di GitHub Actions convalida la pubblicazione, non la compilazione delle sue guide.

## Privacy, licenze e pubblicazione

I file locali vengono elaborati dal browser. **La cache RestedXP e i dati dell'account non vengono caricati da questo progetto.** Il codice del converter e i dati di gioco sono ospitati su GitHub Pages. Quando scegli la cartella WoW, Chrome/Edge deve chiederti il permesso di lettura e scrittura previsto dalle sue protezioni; il tool chiede conferma prima di sostituire una cartella PolestarPack preesistente.

Questo repository non distribuisce guide RestedXP o codici associati ai BattleTag. Usa soltanto guide che hai il diritto di convertire e non distribuire guide di altri senza permesso.

La GUI è rilasciata con licenza MIT. Il motore [polestar-convert](https://github.com/aronjanosch/polestar-convert) è MIT; il compilatore Polestar e i dati utilizzati hanno licenze proprie (incluse GPL-3.0). Gli asset pubblici vengono recuperati durante il workflow GitHub Actions \`.github/workflows/pages.yml\` con \`scripts/vendor_converter.py\`.

Il sito è pubblicato automaticamente su GitHub Pages dopo gli aggiornamenti al ramo \`main\`. La compilazione del sito è verificata da GitHub Actions; la compatibilità con ogni installazione Windows di WoW Forever deve essere verificata sul PC dell'utente.
