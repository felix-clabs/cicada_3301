<?php

namespace App\Commands;

use App\Enums\Rune;
use Illuminate\Support\Str;
use LaravelZero\Framework\Commands\Command;

class AudioToRuneMapper extends Command
{
    protected $signature = 'app:audio-to-rune-mapper {file} {--method=frequency}';

    protected $description = 'Maps audio data (frequencies or amplitude) to a sequence of Runes.';

    public function handle(): int
    {
        $file = $this->argument('file');

        if (!file_exists($file)) {
            $this->error("File not found: $file");
            return self::FAILURE;
        }

        $this->info("Analyzing audio file: $file using method: " . $this->option('method'));

        // Since we don't have sox/ffmpeg, we will simulate the extraction
        // by reading the raw binary data and mapping byte values to Gematria indices
        // as a placeholder for a real FFT analysis.

        $handle = fopen($file, "rb");
        $contents = fread($handle, 1024); // Read first KB for sample
        fclose($handle);

        $runes = '';
        $bytes = unpack("C*", $contents);

        $this->info("Sampled " . count($bytes) . " bytes.");

        foreach (array_slice($bytes, 0, 50) as $byte) {
            $index = $byte % 29;
            $rune = Rune::tryFromIndex($index);
            if ($rune) {
                $runes .= $rune->toRune();
            }
        }

        $this->info("Generated Rune Sequence (first 50 units):");
        $this->line($runes);

        $this->info("Analyzing for prime patterns in bytes...");
        $primeMatches = 0;
        foreach ($bytes as $byte) {
            if ($this->isPrime($byte)) {
                $primeMatches++;
            }
        }
        $this->info("Found $primeMatches prime-valued bytes in sample.");

        return self::SUCCESS;
    }

    private function isPrime($n): bool
    {
        if ($n <= 1) return false;
        for ($i = 2; $i * $i <= $n; $i++) {
            if ($n % $i == 0) return false;
        }
        return true;
    }
}
