# po-translate 1.6.2 i Yeager RPM-repot

## Orsak

GitHub-releasen och PyPI-paketet `po-translate-ai` var redan 1.6.2, men DNF-repot innehöll bara `po-translate` 1.6.1. Görans rapport om en äldre RPM-version stämde därför.

## Genomförd åtgärd

- Releaseflödet i `yeager/po-translate` bygger nu både DEB och RPM i GitHubs Linux-miljö och bifogar filerna till releasen. Ändringen finns på GitHub i commit `a2b873db41866c016cc5a348e277a8e5a36925a9`.
- Workflow-körning [43382135143](https://github.com/yeager/po-translate/actions/runs/43382135143) byggde och laddade upp `po-translate-1.6.2-1.noarch.rpm` till den publicerade releasen `v1.6.2`.
- RPM-repots importlista fick den nya, versionslåsta release-tillgången i commit `bf39b92f39750b15fbdba9b00ab017d8fe7574e0`.
- Importkörning [43382231641](https://github.com/yeager/rpm-repo/actions/runs/43382231641) uppdaterade metadata och publicerade repot. README uppdaterades därefter till 1.6.2 i commit `f0cbd6e837fba96f7470223e58fe7c66af5b5fd6`.
- `po-translate`-README uppdaterades i commit `9c65127` så att DEB-exemplet hämtar 1.6.2 och PyPI-distributionen anges som `po-translate-ai`, inte det separata paketet `po-translate`.

## Verifiering

- Releasefilen är `po-translate-1.6.2-1.noarch.rpm`, 24 965 byte, SHA-256 `fdf926b804f8b448b06949f85d4a1cac371f50e27ba4905b024a4e5c7453dadc`.
- `rpm -qip` bekräftar version 1.6.2, release 1 och `noarch`; paketet använder Linux-sökvägen `/usr/share/licenses/po-translate-1.6.2/`.
- Releaseflödets testsvit: 24 godkända tester.
- RPM-repots egen validering och GitHub Pages-distribution passerade i körning [43382488813](https://github.com/yeager/rpm-repo/actions/runs/43382488813).
- Publicerad `repomd.xml` har korrekt kontrollsumma för primärmetadata. Samtliga 281 RPM-sökvägar som metadata refererar till svarar med HTTP 200.
- Diffkontroll och Gitleaks passerade för de lokala ändringarna före varje överföring till GitHub.

## Aktuellt läge

`https://yeager.github.io/rpm-repo` publicerar `po-translate-1.6.2-1.noarch.rpm`. Den äldre 1.6.1-filen ligger kvar som historisk version, men DNF väljer 1.6.2 som högsta tillgängliga version.
