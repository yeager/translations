# Home Assistant Core: direkt platshållaraudit

Den lokala Core-snapshoten jämfördes med direktlästa Lokalise-översättningar för alla 19 poster där snapshotens källa och mål hade olika `{…}`-platshållare.

- Avvikelser i äldre snapshot: 19.
- Kvarstående avvikelser i direktläst Lokalise: 0.

Resultatet bekräftar de löpande API-sparningarna och visar att äldre snapshotvärden, inte Lokalise, förklarar de kvarvarande varningarna. Ingen ny TMX-post behövs eftersom auditten inte ändrade Lokalise.
