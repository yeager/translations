truncate-about = Minska eller utöka storleken för varje fil till den angivna storleken.
truncate-usage = truncate [FLAGGA]... [FIL]...
truncate-after-help = SIZE är ett heltal med ett valfritt prefix och en valfri enhet.
  De tillgängliga enheterna K, M, G, T, P, E, Z och Y använder följande format:
      'KB' => 1000, kilobyte
      'K' => 1024, kibibyte
      'MB' => 1000*1000, megabyte
      'M' => 1024*1024, mebibyte
      'GB' => 1000*1000*1000, gigabyte
      'G' => 1024*1024*1024, gibibyte
  SIZE kan också föregås av något av följande för att justera storleken för varje
  fil utifrån dess nuvarande storlek:
      '+' => utöka med
      '-' => minska med
      '<' => högst
      '>' => minst
      '/' => avrunda nedåt till multipel av
      '%' => avrunda uppåt till multipel av
truncate-help-io-blocks = behandla SIZE som antalet I/O-block i filen i stället för byte
truncate-help-no-create = skapa inte filer som inte finns
truncate-help-reference = basera storleken för varje fil på storleken för RFILE
truncate-help-size = ange eller justera storleken för varje fil enligt SIZE, som anges i byte om inte --io-blocks har angetts
truncate-error-cannot-open-no-device = kan inte öppna { $filename } för skrivning: ingen sådan enhet eller adress
truncate-error-cannot-open-for-writing = kan inte öppna { $filename } för skrivning
truncate-error-invalid-number = ogiltigt tal: { $error }
truncate-error-must-specify-relative-size = du måste ange en relativ '--size' med '--reference'
truncate-error-division-by-zero = division med noll
truncate-error-cannot-stat-no-such-file = kan inte använda stat på { $filename }: filen eller katalogen finns inte
truncate-error-value-too-large = värdet är för stort för den definierade datatypen
truncate-error-value-too-large-arg = { $arg }: värdet är för stort för den definierade datatypen
truncate-error-io-block-mul-overflow = spill vid { $num } * { $factor } byteblock
