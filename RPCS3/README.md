
Create the folder qt6/translations within the RPCS3 main folder.

Download the rpcs3_empty.ts and rename it to your language code (i.e "fr" for French, like "rpcs3_fr.ts")
Open the file in Qt Linguist and translate it. Do not edit the file in a normal text editor.
Release the file in Linguist to create the .qm file (or use Qt lrelease)

Copy the .qm file to qt6/translations, start RPCS3 and select your language from the Help menu.

.

$ lrelease *ts

Updating 'rpcs3_sv.qm'...

    Genererade 2077 översättningar (2077 slutförda och 0 oavslutade)
    
    Ignorerade 828 oöversatta källtexter
    

![image](https://github.com/user-attachments/assets/7367b87b-fd1e-4d05-b2ed-9085af1d8997)
