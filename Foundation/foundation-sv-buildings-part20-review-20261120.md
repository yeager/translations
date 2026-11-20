# Foundation — svensk granskningsrapport

Datum: 2026-11-20  
Komponent: `buildings.json` (del 20)

| Engelsk källsträng | Tidigare svensk text | Föreslagen svensk text | Lint och stavning |
|---|---|---|---|
| Emissary Office | Sändebudets kontor | Sändebudskontor | Inga anmärkningar. |
| Interior Access | Invändig åtkomst | Inre åtkomst | Inga anmärkningar. |
| Interior is inaccessible | Insidan är inte åtkomlig | Insidan är inte åtkomlig | Inga anmärkningar; redan registrerad i Crowdin. |
| Enclosed area access | Åtkomst till förslutet område | Åtkomst till inhägnat område | Inga anmärkningar. |
| Connect an entrance from the enclosed area to its surrounding interior access. The surrounding interior access must also be connected outside. | Anslut en ingång från det förslutna området till dess omgivande invändig åtkomst. Den omgivande invändiga åtkomsten måste också vara ansluten utifrån. | Anslut en ingång från det inhägnade området till dess omgivande inre åtkomst. Den omgivande inre åtkomsten måste också vara ansluten till utsidan. | Inga anmärkningar. |
| Toggle Interior Access Visibility | Växla synlighet för invändig åtkomst | Växla synligheten för inre åtkomst | Inga anmärkningar. |
| When turned on, Interior Access connected to entrances is highlighted in green, while Interior Access without entrances are highlighted in red and cannot be reached. | När den är påslagen är invändig åtkomst som är anslutet till entréer markerat med grönt, medan inre tillträde utan entréer är markerat med rött och inte kan nås. | När den är påslagen markeras inre åtkomst som är ansluten till ingångar med grönt, medan inre åtkomst utan ingångar markeras med rött och inte kan nås. | Inga anmärkningar. |

`l10n-lint --language sv` godkände filen och `hunspell-sv` fann inga stavningsanmärkningar. Sex förslag skapades med HTTP 201; en identisk text fanns redan i Crowdin. Hunspell gav endast Gettext-varningen om PO-huvudets teckenuppsättning; den gäller inte översättningarna.