cp-after-help = Kopiera inte en fil som inte är en katalog om en befintlig destinationsfil har samma eller nyare ändringstid.
  Hoppa i stället över filen utan att rapportera ett fel. Om tidsstämplar bevaras jämförs
  källtidsstämpeln, avkortad till den upplösning som destinationsfilsystemet och de systemanrop
  som uppdaterar tidsstämplar använder. Det undviker dubbelarbete om flera cp -pu-kommandon
  körs med samma källa och destination. Denna flagga ignoreras om flaggan -n eller --no-clobber
  också anges. Om --preserve=links också anges, som till exempel med cp -au, har den företräde.
  Beroende på i vilken ordning källfilerna behandlas kan därför nyare filer i destinationen ersättas
  för att efterlikna hårda länkar i källan. Det ger mer kontroll över vilka befintliga filer i
  destinationen som ersätts, och värdet kan vara något av följande:

  - all: Detta är standardåtgärden när ingen flagga --update har angetts och innebär att alla befintliga filer i destinationen ersätts.

  - none: Detta liknar flaggan --no-clobber eftersom inga filer i destinationen ersätts, men att hoppa över en fil leder inte heller till fel.

  - older: Detta är standardåtgärden när --update har angetts och innebär att filer ersätts om de är äldre än motsvarande källfil.
