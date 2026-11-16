# Home Assistant Core: Libresync och mallmediespelare, batch 124

Den här batchen omfattar Libresyncs anslutningsflöde och fält för åtgärder i
en mallbaserad mediespelare. UPnP och portnumret behålls som tekniska namn.
Fältet `Muted` följer befintlig Home Assistant-terminologi: `Ljud av`.

Kontroller före inskick:

- JSON och platshållaren `{name}` är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: översättningarna är sparade med Lokalise API och återlästa
efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning
eller en utgåva.
