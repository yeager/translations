install-usage = install [FLAGGA]... [FIL]...
install-error-extra-operand = extra operand { $operand }
  { $usage }
install-help-default-context = ange SELinux-säkerhetskontexten för målfilen och varje skapad katalog till standardtypen
install-help-unprivileged = kräv inte utökade behörigheter för att ändra ägare, grupp eller filflaggor för målet
install-error-not-permitted = kan inte ta bort { $path }: Åtgärden tillåts inte
install-warning-no-strip-with-program = VARNING: --strip-program ignoreras eftersom flaggan -s inte angavs
install-error-existing-file-not-directory = kan inte skapa katalogen { $path }: Filen finns
install-error-backing-up-destroy-source = säkerhetskopiering av { $dest } kan förstöra källan. { $source } kopierades inte
install-error-will-not-overwrite-just-created = skriver inte över nyss skapade { $dest } med { $source }
install-error-target-dir-access = kunde inte komma åt { $path }: { $error }
install-error-target-stat = kunde inte hämta status för { $path }: { $error }
install-error-create-regular-file = kunde inte skapa den vanliga filen { $path }: { $error }
install-warning-context-ignored = --context ignoreras. Den kräver en SELinux-aktiverad kärna
