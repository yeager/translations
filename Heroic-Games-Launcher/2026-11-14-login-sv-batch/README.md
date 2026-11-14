# Heroic Games Launcher, svensk inloggningsbatch

Datum: 14 november 2026

Hosted Weblate har sex tomma svenska strängar i Login Page. De gäller
felmeddelande, fältetikett och instruktioner för itch.io:s API-nyckel samt
inloggning med SID-kod. Deltan använder projektets i18next-nycklar och
bevarar tekniska namn som itch.io, API och SID.

Kontroller före arkivering: JSON-syntax, l10n-lint, svlang, Hunspell-SV,
diffkontroll och Gitleaks. `msgfmt` är inte tillämpligt på JSON. Upstream-
inskick och återläsning kräver Hosted Weblate-skrivåtkomst, som inte finns
i den aktuella miljön.
