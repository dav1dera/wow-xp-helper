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
