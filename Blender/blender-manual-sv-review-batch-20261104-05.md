# Blender Manual: svensk granskningsbatch 5

Datum: 2026-11-04  
Källa: aktuell export av `manual-sv.po`.  
Omfattning: 11 poster i glTF-exportens lista över registrerade tillägg.

Poster som `KHR_materials_clearcoat` och `EXT_mesh_gpu_instancing` är
protokollidentifierare från Khronos glTF-specifikation. De är inte löpande
svensk text och ska därför återges byteidentiskt, med samma pluraländelse,
versaler och understreck som källan. Batchen rättar tidigare måltexter som
hade ändrat identitet eller ersatt en identifierare med en annan.

`l10n-lint` redovisar elva informationsnotiser om identisk källa och måltext.
Det är avsett här och inte en oöversatt användargränssnittstext. `msgfmt`,
svenska skrivregler, Gitleaks och `git diff --check` passerar.

Råexporten ändras inte. Deltafilen sparas för den kommande samlade
manualuppladdningen på 500–1 000 granskade strängar.
