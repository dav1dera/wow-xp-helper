# WoW XP Helper — RestedXP → Polestar OneClick

Web app per **World of Warcraft Forever**, pensata per condividere una conversione delle guide RestedXP già presenti sul proprio PC in un pacchetto Polestar, senza CMD, Python o un secondo sito.

## Apri l'app

**[Avvia WoW XP Helper](https://dav1dera.github.io/wow-xp-helper/)**

> Il link funziona dopo che GitHub Pages è stato abilitato in **Settings → Pages → Source: GitHub Actions** e il workflow Deploy WoW XP Helper è terminato correttamente.

### Procedura

1. Se non hai ancora importato le tue guide in RestedXP, usa il collegamento all'eventuale servizio esterno dalla pagina: il BattleTag e l'import in WoW restano passaggi manuali.
2. Chiudi completamente WoW per salvare la cache delle guide.
3. Apri il sito con **Chrome o Edge aggiornato** e premi **Seleziona WoW e avvia tutto**.
4. Seleziona la cartella `World of Warcraft\_forever_` e autorizza l'accesso del browser. Le impostazioni predefinite includono **Horde + Alliance, Speedrun/Main e Dungeon**.
5. L'app cerca `WTF/Account/.../SavedVariables/RXPGuides.lua` e `Interface/AddOns/RXPGuides`, recupera le guide leggibili, esegue il compilatore Polestar e scarica uno ZIP `PolestarPack_*.zip`.
6. Se il browser permette la scrittura, conferma l'installazione diretta; altrimenti estrai il pacchetto ZIP in `Interface/AddOns`. Riavvia WoW e usa **Polestar → Community guides**.

Le guide disponibili per ciascuna fazione e i livelli coperti dipendono dai file effettivamente presenti: **non è garantita la copertura 1–60 se mancano delle guide**. Il compilatore può scartare guide incompatibili e le segnala nel log.

### Provenienza del generatore online e limiti dell'integrazione

Il sito esterno [Forever Free RXP](https://forever-free-rxp.online/en/) dichiara di basarsi sul Gist pubblico [`decrypt_guide.py` di imSp4rky](https://gist.github.com/imSp4rky/17759ae4bd9a78fdc898c901c2436be1).

Lo script legge un file di importazione RestedXP cifrato, associato a un BattleTag, e può convertirlo in un addon `RXPDecryptedGuides` contenente guide Lua. Il codice pubblico **non contiene alcun pacchetto di guide cifrate** e non offre da solo un servizio di generazione di codici per un nuovo account. Il sito esterno dichiara di usare una propria sorgente di guide: per questo il solo Gist non è sufficiente a replicarlo.

WoW XP Helper **non integra il decrypt/re-encrypt degli import associati a BattleTag**, non acquisisce sorgenti premium di terzi e non distribuisce guide. È un convertitore locale delle guide che ogni utente è autorizzato a utilizzare e che risultano disponibili nella propria installazione.

### Privacy e licenze

- La conversione avviene nel browser; **nessun file RXP viene inviato al server di questo progetto**. Il motore compilato e i dati di gioco sono distribuiti dal sito GitHub Pages in fase di pubblicazione.
- Questo repository **non contiene guide RestedXP, codici BattleTag né cache personali**.
- Il sito esterno [Forever Free RXP](https://forever-free-rxp.online/en/) è soltanto collegato, non incorporato, replicato o automatizzato. Il progetto non è affiliato con quel sito.
- Converti soltanto guide che hai diritto di usare; non ridistribuire guide di terzi senza autorizzazione.
- La UI di questo repository è MIT; **polestar-convert** di [aronjanosch](https://github.com/aronjanosch/polestar-convert) è MIT; il compilatore e i dati Polestar sono soggetti alle proprie licenze GPL-3.0 e a quelle dei dati. Gli asset di conversione sono recuperati durante il deploy da fonti pubbliche e non sono inclusi nel repository.
- L'app richiede Internet per il primo caricamento e l'accesso locale autorizzato dall'utente. In questo momento la conversione e l'installazione finali **non sono state testate end-to-end sul tuo client Windows**.

### Sviluppo e deploy

Il workflow `.github/workflows/pages.yml` prepara il sito usando `scripts/vendor_converter.py`: recupera il codice del converter e il compilatore WebAssembly con i relativi dati di gioco, senza alcun contenuto di guide RestedXP. Fa il deploy su GitHub Pages.

Il pulsante della pagina consente un solo flusso dopo la selezione della cartella WoW, ma il browser richiede autorizzazione esplicita per leggere/scrivere i file e per sostituire un pacchetto già installato. Questo limite di sicurezza non può essere eliminato dal sito.
