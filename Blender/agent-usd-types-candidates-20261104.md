# Kandidater: Blender Manual — USD-datatyper

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`  
Avgränsning: `files/import_export/usd.rst`, raderna 693–729.  
Status: kandidatunderlag; råexport och befintliga batcher är orörda.

## Säkra kandidater

1. `quatf`-beskrivningen har både en grammatiskt trasig ordgrupp och en
   felaktigt använd RST-term. En säker målform som bevarar terminlänken är:

   ```po
   msgid "Floating point :term:`Quaternion` rotation."
   msgstr ":term:`Kvaternionsrotation <Quaternion>` med flyttal."
   ```

   Blender-UI:t har `Quaternion` → `Kvaternion` och `Floating point
   quaternion rotation` → `Kvaternionsrotation med flyttal`.

2. Typbegränsningen behöver både rätt svensk fackform och oförändrade
   kodidentifierare:

   ```po
   msgid ""
   "Blender does not support USD Primvars using 64-bit integer values "
   "(``int64``), those using unsigned types (``uint``), or those using 64-bit"
   " double-precison or 16-bit half-precision floating-point values. For "
   "example, this would include such types as ``matrix4d`` (4x4 matrix of "
   "doubles) and ``quath`` (half-precision quaternion)."
   msgstr ""
   "Blender har inte stöd för USD-primvars som använder 64-bitars "
   "heltalsvärden (``int64``), osignerade typer (``uint``) eller 64-bitars "
   "flyttal med dubbel precision eller 16-bitars flyttal med halv precision. "
   "Det omfattar exempelvis ``matrix4d`` (4×4-matris med flyttal med dubbel "
   "precision) och ``quath`` (kvaternion med halv precision)."
   ```

3. `float4`-begränsningen har felaktig kodformatering och kan förtydligas:

   ```po
   msgid ""
   "The USD ``float4`` data type has no direct Blender equivalent and will "
   "not be treated as a Blender ``Color`` or ``Quaternion``."
   msgstr ""
   "Datatypen USD ``float4`` har ingen direkt motsvarighet i Blender och "
   "behandlas inte som Blenders ``Color`` eller ``Quaternion``."
   ```

## Avsiktligt utelämnade poster

- `float`, `2D Vector`, `color4f` och `Byte Color` är delade `msgid` i
  andra manualavsnitt. De behöver projektomfattande kontroll före ändring.
- `RGBA color ... displayColor ...` och `USD does not provide a byte color
  equivalent ...` är redan föreslagna i batch 22 och granskas där, inte här.
- USD-tillgänglighetsposterna från rad 736 och framåt täcks av batch 12–13.

## Identifierar- och markupregler

Bevara ``int64``, ``uint``, ``matrix4d``, ``quath``, ``float4``, ``Color``
och ``Quaternion`` exakt med dubbla backticks. RST-termens destination
`Quaternion` får inte ändras när dess synliga svenska text lokaliseras.
