# Pending MATE uploads

Updated: 11 October 2026

Fedora Weblate currently locks the two components below. The API rejects updates, so no local change has been uploaded to either component.

## MATE Control Center

- Weblate component: [MATE Control Center](https://translate.fedoraproject.org/projects/mate-desktop/applications/mate-control-center/sv/)
- Current status: locked
- Current export: 1,159 translated strings of 1,159
- Upload state: not ready for upload

The latest server export still needs a local correction pass before it can be uploaded. The outstanding issues are five Nordic keyboard accelerators, missing accelerators, punctuation, percent spacing and trailing whitespace. Command names and interface shortcuts must remain literal where applicable.

## MATE Control Center help

- Weblate component: [MATE Control Center help](https://translate.fedoraproject.org/projects/mate-desktop/help-documentation/mate-control-center-help/sv/)
- Current status: locked
- Current export: 357 translated strings of 357
- Upload state: corrections identified locally but cannot be submitted

The next upload must correct these three items:

1. Remove the comma before “och” in the start tips paragraph.
2. Retain the colon in the sentence beginning “Consequently:”.
3. Remove the final semicolon from the GNU documentation licence text.

Before either component is uploaded, download a fresh server export, reapply only still relevant corrections, then run l10n-lint, msgfmt --check and Gitleaks on the exact upload file.
