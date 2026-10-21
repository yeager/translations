stat-after-help = Giltiga formatsekvenser för filer, utan `--file-system`:

    -`%a`: åtkomsträttigheter oktalt, observera printf-flaggorna '#' och '0'
    -`%A`: åtkomsträttigheter i läsbar form
    -`%b`: antal tilldelade block, se %B
    -`%B`: storleken i byte för varje block som rapporteras av %b
    -`%C`: sträng för SELinux-säkerhetskontext
    -`%d`: enhetsnummer decimalt
    -`%D`: enhetsnummer hexadecimalt
    -`%f`: rått läge hexadecimalt
    -`%F`: filtyp
    -`%g`: ägarens grupp-ID
    -`%G`: ägarens gruppnamn
    -`%h`: antal hårda länkar
    -`%i`: inodnummer
    -`%m`: monteringspunkt
    -`%n`: filnamn
    -`%Qn`: citerat filnamn
    -`%N`: citerat filnamn med dereferering, följning, om det är en symbolisk länk
    -`%o`: rekommenderad optimal I/O-överföringsstorlek
    -`%s`: total storlek i byte
    -`%t`: huvudenhetstyp hexadecimalt för specialfiler av tecken- eller blockenhetstyp
    -`%T`: underenhetstyp hexadecimalt för specialfiler av tecken- eller blockenhetstyp
    -`%u`: ägarens användar-ID
    -`%U`: ägarens användarnamn
    -`%w`: filens födelsetid i läsbar form, - om den är okänd
    -`%W`: filens födelsetid, sekunder sedan epoken, 0 om den är okänd
    -`%x`: tidpunkt för senaste åtkomst i läsbar form
    -`%X`: tidpunkt för senaste åtkomst, sekunder sedan epoken
    -`%y`: tidpunkt för senaste dataändring i läsbar form
    -`%Y`: tidpunkt för senaste dataändring, sekunder sedan epoken
    -`%z`: tidpunkt för senaste statusändring i läsbar form
    -`%Z`: tidpunkt för senaste statusändring, sekunder sedan epoken

  Giltiga formatsekvenser för filsystem:

    -`%a`: lediga block tillgängliga för icke-superanvändare
    -`%b`: totalt antal datablock i filsystemet
    -`%c`: totalt antal filnoder i filsystemet
    -`%d`: lediga filnoder i filsystemet
    -`%f`: lediga block i filsystemet
    -`%i`: filsystems-ID hexadecimalt
    -`%l`: maximal längd för filnamn
    -`%n`: filnamn
    -`%Qn`: citerat filnamn
    -`%s`: blockstorlek, för snabbare överföringar
    -`%S`: grundläggande blockstorlek, för blockantal
    -`%t`: filsystemstyp hexadecimalt
    -`%T`: filsystemstyp i läsbar form

  OBS: Ditt skal kan ha en egen version av stat som vanligtvis har företräde
  framför versionen som beskrivs här. Läs skalets dokumentation för uppgifter
  om de flaggor som versionen stöder.
