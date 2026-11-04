# Oberoende teknisk granskning: Blender Manual, batch 11–16

Datum: 2026-11-04  
Granskade filer: `blender-manual-sv-review-batch-20261104-11.po` till och
med `blender-manual-sv-review-batch-20261104-16.po`.

## Resultat

- Samtliga 40 deltaposters `msgid` matchar en post i den orörda
  råexporten `exports/2026-11-04/blender-manual-manual-sv.po` exakt.
- `msgfmt --check` godkänner alla sex filer.
- `l10n-lint` rapporterar inga fel eller varningar. Informationsnivåns
  träffar för `USD` är falska positiva valutaträffar.
- URL:er samt destinationer i `:doc:`- och `:ref:`-roller är bevarade.

## Åtgärd krävs

I batch 14 skrivs den kodformaterade pluralformen ``Scopes`` i källan som
``Scope``-primitiver i måltexten. Formuleringen är läsbar svenska, men den
ändrar en kodformaterad källterm. För maximal teknisk trohet bör en
uppföljningsdelta använda exempelvis:

```po
msgid ""
"USD also supports ``Scope`` primitives, which are entities that do not "
"contain transform data, but which serve to group other element of the "
"scene. Blender doesn't have an exact counterpart to the concept of a "
"scope, so such primitives are imported as Blender empties located at the "
"origin. This is an imperfect representation, because empty objects have a"
" transform and ``Scopes`` do not, but this approach nonetheless helps "
"preserve the structure of the scene hierarchy."
msgstr ""
"USD stöder även ``Scope``-primitiver, som är enheter utan transformdata "
"och som används för att gruppera andra scenelement. Blender har ingen "
"direkt motsvarighet till scope-begreppet, så sådana primitiver importeras "
"som tomma Blender-objekt vid origo. Det är en ofullständig representation, "
"eftersom tomma objekt har en transform medan ``Scopes`` saknar en sådan, "
"men detta bevarar ändå scenhierarkins struktur."
```

## Godkända avvikelser

Batch 13 delar upp den källformaterade listan ``low, standard, high`` i
tre separata kodformaterade värden. Det förändrar inte något identifierare
eller värde och gör svenskans uppräkning tydligare. Avvikelsen godkänns.

Batch 16 är en spårbar följdrättelse av batch 15 och har korrekt `msgid`
samt inga markupskillnader.
