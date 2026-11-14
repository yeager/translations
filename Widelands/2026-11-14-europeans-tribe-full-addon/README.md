# Widelands Add-Ons: Europeans Tribe (Full Addon)

Den aktuella Widelands-utgåvan är 1.3.1 från 2026-02-22. Elva nya svenska
strängar i resursen `europeans_tribe.wad` granskades i källkodens konkreta
spelkontext: byggnadsnamn, varubeskrivningar och utbildningsnotiser.

- Resurs: `o:widelands:p:widelands-addons:r:europeans-tribe-wad`
- Språk: svenska (`sv`)
- Omfattning: 11 tidigare oöversatta strängar
- Upstream-inskick: Transifex redigerare, 2026-11-14
- Återläsning: filtret `translated:no` visade 0 strängar och alla 11 måltexter
  överensstämde exakt med batchen.

Kontroller före inskick: källkodskontext, `svlang`, Hunspell-sv och
Transifex egen spar- och återläsning. Efter inskicket kontrollerades den
arkiverade deltafilen också med `msgfmt`, `l10n-lint`, diffkontroll och
Gitleaks, utan fel eller läckfynd. Hunspell-sv markerar endast `tabard`;
svlang markerar felaktigt den samordnade nominalfrasen som ett V2-problem.
`tabard` behålls som etablerad
Widelands-term; den används redan i den svenska katalogen. Inga tankstreck
har lagts till i svenskan.

Detta bevisar att de elva strängarna är sparade upstream. Den övergripande
granskningsstatusen för hela resursen är separat: kontot saknar
granskningsbehörighet och Transifex visar därför fortfarande ogranskade
översättningar.
