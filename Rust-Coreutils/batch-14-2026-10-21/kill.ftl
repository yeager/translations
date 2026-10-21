kill-error-write = skrivfel: { $error }
kill-after-help-windows = Anmärkningar om Windows:
  Signalerade processer tvångsavslutas eftersom Windows saknar signalleverans.
  Deras avslutningsstatus är 128 plus signalnumret. Negativa PID:er, en annan
  processgrupp, och STOP stöds inte. Behörigheter hämtas från din aktuella
  token, med SeDebugPrivilege aktiverad när den innehas. Kör med förhöjd
  behörighet för att nå processer som en standardtoken inte kan signalera.
  Skyddade processer, till exempel processer mot skadlig programvara, kan
  inte avslutas alls.

  PID 0 riktar sig mot jobbobjektet som kill körs i, den närmaste
  Windowsmotsvarigheten till en processgrupp. Varje process i jobbet och dess
  underordnade jobb signaleras, kill självt sist, så kill avslutas med gruppen.
  Utanför ett jobb signalerar PID 0 endast kill självt.

  Observera: ett jobbobjekt är vanligtvis inte ditt. Terminaler, IDE:er,
  Docker, CI agenter och Windows egna Program Compatibility Assistant kör
  allt de startar i ett jobb, och ett jobb omfattar alla underordnade processer
  från skapandet och framåt. Under en CI agent signalerar kill 0 agenten och
  varje parallellt steg. Konsekvenserna kan sträcka sig mycket längre än för
  en POSIX processgrupp.
kill-error-unsupported-signal = signal stöds inte på Windows
kill-error-negative-pid-unsupported = en negativ PID, en annan processgrupp, stöds inte på Windows
