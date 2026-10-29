# Bitwarden Web – Crowdin-insändning 2026-10-29, batch 2

- Underlag: `bitwarden-web-sv-crowdin-20261029-batch02.json` med 20
  kontextgranskade strängar för åtkomstbegäranden.
- Kontroller: JSON-syntax, platshållare, `l10n-lint`, Hunspell och Gitleaks.
  `svlang` och `l10n-lint` markerar komponentnyckeln
  `pamApprovalsActiveAccessSection`, inte den svenska måltexten; det är ett
  känt falskt positivt för den maskinella trippelkonsonantkontrollen.
- Skickat som Crowdin-förslag från `yeagersthlm` och bekräftat genom
  editorstatusen ”No unsaved translations”.
- Crowdin markerar korrekt böjda svenska former som `begäranden` och
  `sparas` som terminologi- respektive stavningsvarningar. De är inte
  faktiska svenska språkfel och ändrades inte för att passa kontrollen.
