mv-after-help = När mer än en av flaggorna -i, -f och -n anges får endast den sista effekt.

    Flytta inte en annan fil än en katalog till en befintlig destination med samma eller
    nyare ändringstid.
    Hoppa i stället över filen utan fel. Vid flytt över filsystemsgränser jämförs källans tidsstämpel,
    avkortad till upplösningen hos destinationsfilsystemet och systemanropen som uppdaterar tidsstämplar.
    Det undviker dubbelarbete om flera kommandon mv -u körs med samma källa och destination. Flaggan ignoreras
    om -n eller --no-clobber också anges. Värdet kan vara något av följande:

      - all är standard när --update inte anges och ersätter alla befintliga destinationsfiler.
      - none liknar --no-clobber: inga destinationsfiler ersätts och en överhoppad fil ger inget fel.
      - older är standard när --update anges och ersätter filer som är äldre än motsvarande källfil.
