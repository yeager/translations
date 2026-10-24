# ComfyUI svensk ombasning, manuell batch 4

Batchen omfattar 64 texter för avgränsningsrutor, kameravinklar, enkätflöde,
kontextmenyer och krediter.

Kontroller: JSON-parsning, platshållarjämförelse, svlang, l10n-lint 1.23.27
och avgränsad Gitleaks. Antalet saknade `main.json`-nycklar minskade från 626
till 562.

Tolv nya kameranycklar saknar ännu användning i ComfyUI:s källkod. Det är en
upstream-varning och påverkar inte översättningskatalogens giltighet.
