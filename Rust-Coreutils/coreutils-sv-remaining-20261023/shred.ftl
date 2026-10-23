shred-after-help = Ta bort FILER om --remove (-u) anges. Som standard tas filerna inte bort,
    eftersom det är vanligt att arbeta med enhetsfiler som /dev/hda och sådana
    filer vanligen inte bör tas bort.

    VARNING: shred bygger på ett mycket viktigt antagande: att filsystemet
    skriver över data på plats. Det är det traditionella sättet, men många moderna
    filsystemsutformningar uppfyller inte detta antagande. Följande är exempel på
    filsystem där shred inte är effektivt eller inte med säkerhet är effektivt
    i alla filsystemlägen:

      - loggstrukturerade filsystem eller journalfilsystem, exempelvis de som levereras med
        AIX och Solaris samt JFS, ReiserFS, XFS och Ext3

      - filsystem som skriver redundanta data och fortsätter även om vissa skrivningar
        misslyckas, exempelvis RAID-baserade filsystem

      - filsystem som skapar ögonblicksbilder, exempelvis Network Appliances NFS-server

      - filsystem som mellanlagrar på tillfälliga platser, exempelvis NFS
        version 3-klienter

      - komprimerade filsystem

    För filsystem av typen ext3 gäller ovanstående friskrivning och shred har då
    begränsad effektivitet endast i läget data=journal, där filinnehållet journalförs
    utöver metadata. I standardläget data=ordered och läget data=writeback
    fungerar shred som vanligt. Ext3:s journallägen kan ändras genom att lägga till
    flaggan data=något bland monteringsflaggorna för ett visst filsystem i filen
    /etc/fstab enligt dokumentationen i manualsidan för mount (`man
    mount`).

    Dessutom kan säkerhetskopior av filsystem och fjärrspeglar innehålla kopior av
    filen som inte kan tas bort och som senare gör det möjligt att återställa
    en överskriven fil.
