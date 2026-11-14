# Weblate: inskickningskontroll 2026-11-14

- ADNS, `nextdns-strings`: den tidigare återstående enheten `221097844` är nu
  sparad i Hosted Weblate med en svensk måltext och status `translated`.
  Den behövde därför inte skrivas över.
- Barcode Buddy, `strings`: den lokalt granskade batchen omfattar 32 strängar.
  Ett nytt, explicit PATCH-försök mot enhet `68246127` returnerade HTTP 403
  med `permission_denied`: `This translation is currently locked.` Ingen
  sträng kunde sparas och batchen ligger kvar oförändrad i arkivet.

Övriga här arkiverade Hosted Weblate-batcher har redan statusen mottagen och
återläst. Barcode Buddy kräver att projektadministratören låser upp den
svenska komponenten innan inskick kan genomföras.
