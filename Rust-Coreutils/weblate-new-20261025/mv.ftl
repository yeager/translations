
mv-after-help =
    Om fler än en av flaggorna -i, -f och -n anges gäller endast den sista.
    
    Flytta inte en fil som inte är en katalog om målfilen har samma eller
    nyare ändringstid. Hoppa i stället tyst över filen utan att ge ett fel.
    Vid flytt mellan filsystem jämförs källans tidsstämpel efter avkortning
    till den upplösning som målfilsystemet och systemanropen för att ändra
    tidsstämplar har. Det undviker dubbelarbete när flera mv -u-kommandon körs
    med samma källa och mål. Flaggan ignoreras om -n eller --no-clobber anges.
    Värdet styr vilka befintliga målfiler som ersätts och kan vara:
    
    - all: ersätt alla befintliga målfiler; standard när --update inte anges.
    - none: ersätt inga målfiler; som --no-clobber, men utan fel om en fil hoppas över.
    - older: ersätt filer som är äldre än källfilen; standard när --update anges.
