# Pending Transifex updates

The seven corrections in `dolphin-emulator-sv-pending-reviewed-lock-20261011.po`
were validated with `msgfmt`, `l10n-lint`, Hunspell review, and Gitleaks.

Transifex currently returns HTTP 403 for each change because the affected Swedish
translations are marked as reviewed. The account may read the resource but may not
alter reviewed entries. Upload these corrections after a project reviewer unreviews
the entries or grants the account permission to edit reviewed translations.
