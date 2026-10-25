shred-after-help =
    Ta bort FILER om --remove (-u) anges. Som standard tas filerna inte bort,
    eftersom det är vanligt att arbeta med enhetsfiler som /dev/hda och sådana
    filer vanligen inte bör tas bort.
    
    VARNING: shred bygger på ett viktigt antagande: att filsystemet skriver över
    data på plats. Det är det traditionella sättet, men många moderna filsystem
    uppfyller inte antagandet. Följande är exempel på filsystem där shred inte
    är effektivt eller inte säkert är effektivt i alla filsystemlägen:
    
     - loggstrukturerade filsystem eller journalförande filsystem, exempelvis de
       som levereras med AIX och Solaris samt JFS, ReiserFS, XFS och Ext3
    
     - filsystem som skriver redundanta data och fortsätter även om vissa
       skrivningar misslyckas, exempelvis RAID-baserade filsystem
    
     - filsystem som skapar ögonblicksbilder, exempelvis Network Appliances NFS-server
    
     - filsystem som mellanlagrar data, exempelvis klienter för NFS version 3
    
     - komprimerade filsystem
    
    För ext3-filsystem gäller begränsningen ovan endast i läget data=journal,
    som journalför filinnehåll utöver metadata. I lägena data=ordered (standard)
    och data=writeback fungerar shred som vanligt. Ext3:s journalläge kan ändras
    genom att lägga till flaggan data=något bland monteringsflaggorna för ett
    filsystem i /etc/fstab, enligt manualsidan för mount (`man mount`).
    
    Säkerhetskopior av filsystem och fjärrspeglar kan dessutom innehålla kopior
    av filen som inte kan tas bort och som gör det möjligt att återställa den
    efter att shred har körts.
