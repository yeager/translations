# Foundation — svensk granskningsrapport

Datum: 2026-11-20  
Komponent: `military.release.json` (del 5)

| Engelsk källsträng | Tidigare svensk text | Föreslagen/sparad svensk text | Lint och stavning |
|---|---|---|---|
| The Combatant is Fully Trained: They will earn plenty of Experience and are unlikely to be harmed during missions. | En kombattant är fullt utbildad: De kommer att tjäna massor av erfarenhet och kommer sannolikt inte att skadas under uppdrag. | Den stridande är fullt utbildad: Personen får gott om erfarenhet och kommer sannolikt inte att skadas under uppdrag. | Inga anmärkningar. |
| Combatant Rank | Kombattantrang | Den stridandes rang | Inga anmärkningar. |
| Combatant Happiness | Kombattantlycka | Den stridandes lycka | Inga anmärkningar. |
| This Combatant needs {1} Experience to progress to the next Rank. | Denna kombattant behöver {1} erfarenhet för att gå vidare till nästa rang. | Den stridande behöver {1} erfarenhet för att gå vidare till nästa rang. | Inga anmärkningar; `{1}` bevarad. |
| This Combatant has reached the highest {1} Rank. | Denna kombattant har nått den högsta {1} rangen. | Den stridande har nått den högsta {1} rangen. | Inga anmärkningar; `{1}` bevarad. |
| Combatant Strength | Kombattantstyrka | Den stridandes styrka | Inga anmärkningar. |
| Strength is the combat capability of an individual Combatant. Rank, Weapon Strength, and Training Conditions improve Combatant Strength. | Styrka är en enskild stridande parts stridsförmåga. Rang, vapenstyrka och träningsförhållanden förbättrar kombattantstyrkan. | Styrka är en enskild stridandes stridsförmåga. Rang, vapenstyrka och träningsförhållanden förbättrar den stridandes styrka. | Inga anmärkningar; radbrytningen bevarad. |
| Weapons might break and Combatants might not return from this mission. | Vapen kan gå sönder och Stridande kanske inte återvänder från detta uppdrag. | Vapen kan gå sönder och stridande kanske inte återvänder från detta uppdrag. | Inga anmärkningar. |

`l10n-lint --language sv` godkände PO-filen och `hunspell-sv` fann inga stavningsanmärkningar. Samtliga åtta ändringar skickades via Crowdin API och skapades med HTTP 201. Hunspell gav endast Gettext-varningen om PO-huvudets teckenuppsättning; den gäller inte översättningarna.