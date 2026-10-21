base32-about = Koda och avkoda data och skriv ut dem till standard ut.
  Läs standard in om ingen FIL anges eller om FIL är -.

  Data kodas enligt beskrivningen av Base32-alfabetet i RFC 4648.
  Vid avkodning kan indata innehålla radbrytningar utöver bytena i det
  formella Base32-alfabetet. Använd --ignore-garbage för att försöka
  återställa från andra byte som inte ingår i alfabetet i den kodade
  strömmen.
base32-usage = base32 [FLAGGA]... [FIL]
base64-about = Koda och avkoda data och skriv ut dem till standard ut.
  Läs standard in om ingen FIL anges eller om FIL är -.

  Data kodas enligt beskrivningen av Base64-alfabetet i RFC 3548.
  Vid avkodning kan indata innehålla radbrytningar utöver bytena i det
  formella Base64-alfabetet. Använd --ignore-garbage för att försöka
  återställa från andra byte som inte ingår i alfabetet i den kodade
  strömmen.
base64-usage = base64 [FLAGGA]... [FIL]
basenc-about = Koda och avkoda data och skriv ut dem till standard ut.
  Läs standard in om ingen FIL anges eller om FIL är -.

  Vid avkodning kan indata innehålla radbrytningar utöver bytena i det
  formella alfabetet. Använd --ignore-garbage för att försöka återställa
  från andra byte som inte ingår i alfabetet i den kodade strömmen.
basenc-usage = basenc [FLAGGA]... [FIL]
basenc-help-base64 = samma som programmet 'base64'
basenc-help-base64url = kodning med Base64 som är säker för filer och webbadresser
basenc-help-base32 = samma som programmet 'base32'
basenc-help-base32hex = Base32 med utökat hexadecimalt alfabet
basenc-help-base16 = hexadecimal kodning
basenc-help-base2lsbf = bitsträng med minst signifikanta biten (lsb) först
basenc-help-base2msbf = bitsträng med mest signifikanta biten (msb) först
basenc-help-z85 = kodning som liknar ascii85;
  vid kodning måste inmatningens längd vara en multipel av 4;
  vid avkodning måste inmatningens längd vara en multipel av 5
basenc-help-base58 = Base58-kodning som inte kan misstolkas visuellt
basenc-error-missing-encoding-type = kodningstyp saknas
base-common-extra-operand = extra operand { $operand }
base-common-no-such-file = { $file }: filen eller katalogen finns inte
base-common-invalid-wrap-size = ogiltig radbrytningslängd: { $size }
base-common-read-error = läsfel: { $error }
base-common-invalid-input = ogiltiga indata
base-common-help-decode = avkoda data
base-common-help-ignore-garbage = ignorera tecken som inte ingår i alfabetet vid avkodning
base-common-help-wrap = radbryt kodade rader efter COLS tecken (standard { $default }, 0 för att inaktivera radbrytning)
