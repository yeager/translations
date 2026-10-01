# Keycloak Swedish Weblate review — 2026-10-01

All current Keycloak Swedish Weblate components were reviewed. The 23 untranslated strings were translated and submitted through Weblate; the two strings marked for rewriting were reviewed and updated.

Weblate status after submission: every component is 100% translated, with no fuzzy strings and no failing translation checks.

`admin-ui.properties` contains one inherited upstream source unit without a Java-properties key (`the attribute. For that, …`). It is emitted as a bare line in the export, so `l10n-lint` correctly reports a syntax error. This is a source-catalog defect, not a Swedish translation error, and cannot be corrected in the target translation without altering the source structure.
