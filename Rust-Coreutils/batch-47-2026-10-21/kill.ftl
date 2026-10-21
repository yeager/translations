kill-after-help-windows = Anmärkningar om Windows:
  Processer som signaleras tvångsavslutas, eftersom Windows inte levererar signaler.
  Deras avslutningsstatus är 128 plus signalnumret. Negativa PID:er, en annan
  processgrupp, och STOP stöds inte. Behörigheterna hämtas från din aktuella
  åtkomsttoken. SeDebugPrivilege aktiveras om den finns. Kör med förhöjd
  behörighet för att nå processer som inte kan signaleras med en standardtoken.
  Skyddade processer, till exempel mot skadlig programvara, kan inte avslutas alls.

  PID 0 riktar sig mot jobbobjektet som kill körs i, Windows närmaste motsvarighet
  till en processgrupp. Varje process i jobbet och dess underordnade jobb signaleras,
  med kill självt sist, så kill avslutas med gruppen. Utanför ett jobb signalerar
  PID 0 bara kill självt.

  Varning: ett jobbobjekt är vanligen inte ditt. Terminaler, IDE:er, Docker, CI-
  agenter och Windows eget Program Compatibility Assistant kör det de startar
  i ett jobb, och ett jobb omfattar alla underordnade processer från det att det
  skapas. Under en CI-agent signalerar kill 0 agenten och varje parallellt steg.
  Följderna kan bli betydligt större än för en POSIX-processgrupp.
