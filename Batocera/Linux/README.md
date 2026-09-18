Connect to Batocera via WinSCP (or via SSH).

Copy the emulationstation2.mo file to /usr/share/locale/sv_SE/LC_MESSAGES/ 

On a keyboard connected to the Batocera machine, press [Alt] + [F4] (or run batocera-es-swissknife --restart if in SSH) to refresh the language strings in ES.

Now explore ES to view all the strings you've translated!

To keep your changes persistent between reboots, connect via SSH if you haven't already and run batocera-save-overlay to save the overlay.
