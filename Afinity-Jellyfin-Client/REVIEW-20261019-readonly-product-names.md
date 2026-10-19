# Afinity Swedish read-only product-name strings — 2026-10-19

`l10n-lint` reports empty product-name strings in the downloaded PO catalog. Weblate confirms these strings are upstream read-only, with disabled edit and submit controls. For example, `service_name_jellyseerr` has English source `Jellyseerr`, an empty Swedish target, and state `Read-only`.

The component dashboard reports 18 read-only strings. They count as translated for Weblate coverage (3,010/3,010) but remain empty in the PO file, so local lint reports them as missing. They cannot be corrected through the Swedish Weblate component; the upstream component must change their review state or provide targets.
