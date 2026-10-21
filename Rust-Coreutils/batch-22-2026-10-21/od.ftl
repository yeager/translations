od-after-help = Visar data i olika läsbara format. Om flera format anges innehåller utdata
  alla format i den ordning de står på kommandoraden. Varje format skrivs ut på en ny
  rad. Endast raden som innehåller det första formatet får prefixet offset.

  Om inget filnamn anges, eller om filnamnet är "-", används standardindata. Efter "--"
  tolkas inga fler flaggor. Det gör att filnamn som börjar med "-" kan användas.

  Om ett filnamn är ett giltigt tal som kan användas som offset i den andra formen kan
  du tvinga att det tolkas som ett filnamn genom att ange en flagga som "-j0", som endast
  är giltig i den första formen.

  RADIX är ett av o,d,x,n för oktal, decimal, hexadecimal eller inget.

  BYTES är decimal som standard, oktal om det inleds med "0" och hexadecimalt om det
  inleds med "0x". Suffixen b, KB, K, MB, M, GB och G multiplicerar talet med 512,
  1000, 1024, 1000^2, 1024^2, 1000^3, 1024^3, 1000^2 respektive 1024^2.

  OFFSET och LABEL är oktala som standard, hexadecimala om de inleds med "0x" eller
  decimala om suffixet "." läggs till. Suffixet "b" multiplicerar med 512.

  TYPE innehåller en eller flera formatspecifikationer som består av:
      a för utskrivbar 7 bitars ASCII
      c för UTF-8 tecken eller oktal för odefinierade tecken
      d[SIZE] för decimal med tecken
      f[SIZE] för flyttal
      o[SIZE] för oktal
      u[SIZE] för decimal utan tecken
      x[SIZE] för hexadecimal
  SIZE är antalet byte, vilket kan vara 1, 2, 4, 8 eller 16,
      eller C, S, I, L för 1, 2, 4, 8 byte för heltalstyper,
      eller F, D, L för 4, 8, 16 byte för flyttal.
  Varje typspecifikation kan ha suffixet "z", som lägger till en ASCII dump i slutet
      av raden.

  Om ett fel uppstår skrivs ett diagnostiskt meddelande till standardfel och
  avslutningskoden blir nollskild.
