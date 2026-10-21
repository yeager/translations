numfmt-after-help = Alternativ för UNIT:

  - none: ingen automatisk skalning utförs, suffix ger ett fel

  - auto: godta valfritt suffix med en eller två bokstäver:

      1K = 1000, 1Ki = 1024, 1M = 1000000, 1Mi = 1048576,

  - si: godta valfritt suffix med en bokstav:

      1K = 1000, 1M = 1000000, ...

  - iec: godta valfritt suffix med en bokstav:

      1K = 1024, 1M = 1048576, ...

  - iec-i: godta valfritt suffix med två bokstäver:

      1Ki = 1024, 1Mi = 1048576, ...

  - FIELDS stöder fältintervall i stil med cut(1):

      N N:te fältet, räknat från 1
      N- från N:te fältet till radslutet
      N-M från N:te till M:te fältet, inklusive
      -M från första till M:te fältet, inklusive
      - alla fält

  Flera fältintervall kan avgränsas med kommatecken

  FORMAT måste passa för utskrift av ett flyttalsargument, %f.
  Valfritt citattecken (%'f) aktiverar --grouping, om aktuell språkinställning stöder det.
  Ett valfritt breddvärde (%10f) fyller ut utdata. En valfri nolla i bredden (%010f)
  fyller ut talet med nollor. Negativa värden (%-10f) vänsterjusterar. En valfri
  precision (%.1f) ersätter den precision som bestäms av indata.

numfmt-error-write = fel vid skrivning
