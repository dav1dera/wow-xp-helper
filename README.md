# WoW XP Helper

**RestedXP → Polestar con un solo pulsante**, per chi gioca a WoW Forever.

### [Apri WoW XP Helper](https://dav1dera.github.io/wow-xp-helper/)

## Come si usa

1. **Hai già le guide RestedXP aggiornate?** Puoi saltare il primo passaggio della pagina. Verifica la versione delle guide per la tua lingua. Le risorse esterne sono elencate nella pagina in quest'ordine: [Inariaa RXP Decrypter](https://inariaa.github.io/rxp_decrypter/) e [Forever Free RXP](https://forever-free-rxp.online/en/) come alternativa. Usa soltanto guide per le quali disponi dei necessari diritti. **Prima di sostituire guide già importate**, in WoW usa RestedXP → Import Guide → **Purge**, conferma e premi **Reload**; poi incolla il nuovo codice, premi **Import** e nuovamente **Reload**. *Attenzione: Purge elimina tutte le guide importate.*
2. **Chiudi completamente WoW** in modo che la cache delle guide venga salvata.
3. Premi **Scegli WoW e crea le guide**. Seleziona la cartella \`World of Warcraft\` oppure \`_forever_\`, e autorizza l'accesso ai file nel browser.
4. Il tool recupera le guide presenti sul PC, le converte, compila il pacchetto con il motore di Polestar, scarica uno ZIP e prova a installare i nuovi addon con il tuo consenso.
5. Riavvia WoW e apri **Polestar → Community guides**.

**Se Chrome segnala “Can't open this folder ... contains system files”:** è un blocco di sicurezza del browser. Nella schermata principale usa **Chrome blocca la cartella? Usa il metodo compatibile**: scegli il file `WTF/Account/<account>/SavedVariables/RXPGuides.lua` e poi la cartella `Interface/AddOns/RXPGuides`, infine premi **Crea pacchetto Polestar**. Lo ZIP ottenuto va estratto manualmente in `Interface/AddOns` perché questa modalità non concede accesso in scrittura alla cartella del gioco. Non disattivare le protezioni di Chrome.

**Requisiti:** Chrome o Edge aggiornato su Windows, RestedXP e Polestar già installati nel gioco. Il browser deve supportare la selezione delle cartelle locali. Se la modalità automatica non trova i file, il pannello **Impostazioni avanzate** include un caricamento manuale. Le guide convertite possono differire dall'originale e alcune possono essere escluse dal compilatore.

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
