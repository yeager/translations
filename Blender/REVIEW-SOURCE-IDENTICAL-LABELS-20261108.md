# Blender UI – källidentiska etiketter, urval 2026-11-08

Den lokala Blender UI-exporten innehåller 771 översättningar som är identiska
med källsträngen. De får inte bulkändras: merparten är formella Blender-namn,
API-identifierare, standarder, format, algoritmer eller svenska/engelska
fackord med samma etablerade form.

Följande urval har granskats med respektive konkret användningskontext och
lämnas oförändrat:

| Sträng | Kontext | Beslut |
| --- | --- | --- |
| Action | Blenders formella animeringsdatatyp | Behåll produktnamnet. |
| Slot | Action- och Dope Sheet-kontext | Behåll etablerad Blender-term. |
| Outliner | Blenders redigerarområde | Behåll produktnamnet. |
| Shrinkwrap | begränsnings- och modifierartyp | Behåll synligt funktionsnamn. |
| OpenGL, DirectX, Vulkan | normalmappning/GPU-bakände | Behåll standard- och API-namn. |
| ACES, Rec. 709, ProRes, WebP | färgrymd, kodek och format | Behåll exakta värde- och formatnamn. |
| Status, Definition, Vibration, Modal | UI- och XR-egenskaper | Orden är redan svenska etablerade fackformer. |
| Layout, Rendering | arbetsytemallar | Behåll etablerade synliga Blender-namn. |
| Skinning | glTF-export | Behåll tills en svensk Blender-/glTF-term är belagd; det avser export av skelett- och ledpåverkansdata, inte ett allmänt verb. |

Detta är en granskningsnotering, inte en importdeltafil. Den förhindrar att
identiska strängar behandlas som falska positiva bara för att de innehåller
engelsk stavning.

Källkontroll för Skinning: [Blender Manual: glTF 2.0, Data – Skinning](https://docs.blender.org/manual/en/latest/addons/scene_gltf2.html).
