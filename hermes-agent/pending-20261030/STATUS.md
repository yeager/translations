# Hermes Agent: pågående svenska kataloger

Datum: 2026-10-30.

Detta är en återställningskopia av tre oinscheckade svenska kataloger från
den lokala arbetskopian. De hör **inte** till den redan inskickade,
avsiktligt partiella desktopkatalogen i PR #101116 och ska inte beskrivas som
uppströmsarbete.

| Fil | SHA-256 | Status |
| --- | --- | --- |
| `static-sv.yaml` | `451194825ae203369ad22e43d99147a4698ef87a1b8fa9a5e7f5b8cd423b003a` | YAML kan tolkas; behöver nyckelparitet och kontextgranskning. |
| `tui-sv.ts` | `65587cb773a91479afff848c79ab8101dc312cf43510edf14193a961cc62066f` | Behöver typkontroll, tester och radgranskning mot den engelska katalogen. |
| `web-sv.ts` | `754bb731e87c8b69a9aa3a54f0b7a19eaf1704b60c4889f5dfebc3fd89b0b19d` | Behöver typkontroll, tester och radgranskning mot den engelska katalogen. |

Gitleaks hittade inga hemligheter i någon av filerna. Ingen av dessa filer har
pushats eller skickats uppströms i detta steg.
