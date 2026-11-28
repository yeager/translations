# Hunspell-undantag för WebKitGTK

`hunspell -d sv_SE -l` flaggar följande ord. De är avsiktliga standardnamn, tekniska termer, förkortningar eller produktiva svenska sammansättningar i denna katalog; de har kontrollerats manuellt.

- **Webb/API och varumärken:** `EncryptedMedia`, `IndexedDB`, `MediaCapabilities`, `MediaSource`, `MediaStream`, `WebAudio`, `WebCrypto`, `WebGL`, `WebKitGTK`, `WebRTC`, `JSC`, `Apple Pay`, `TLS`, `MIME`, `XSS`, `stdout`.
- **Unicode-kontroller:** `LRE`, `LRM`, `LRO`, `RLE`, `RLM`, `RLO`, `ZWJ`, `ZWNJ`, `ZWS`; svenska beskrivningar som `Nollbreddsblanksteg`, `Nollbreddssammanfogare` och `Nollbreddsicke-sammanfogare`.
- **Sammansättningar och facktermer:** `JSC-alternativ`, `MIME-typen`, `MediaStream-innehåll`, `WebAudio-innehåll`, `WebCrypto-nycklar`, `WebRTC-innehåll`, `WebKitGTK-lösenord`, `XSS-granskning`, `Piktogramtypsnittsfamilj`, `breddsteg`, `dokumentmarkup`, `flikpanel`, `mediakontroller`, `mediastatistik`, `monospace-typsnitt`, `omritningsräknare`, `sidcache`, `tabb-navigering`, `webbvyn`, `ping` och `pingar`.
- **Böjningsstreck i samordnade sammansättningar:** `datum-`, `månads-` och `vecko-` i uttryck som ”datum- och tidsfält”.
- `Pay` flaggas när Hunspell delar upp varumärket Apple Pay.

`hunspell-output.txt` sparar den fullständiga ordlistan från verktyget efter den slutliga granskningen.
