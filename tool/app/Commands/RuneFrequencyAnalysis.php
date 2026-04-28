<?php

namespace App\Commands;

use App\Enums\Rune;
use Illuminate\Support\Str;
use LaravelZero\Framework\Commands\Command;

class RuneFrequencyAnalysis extends Command
{
    protected $signature = 'app:rune-frequency-analysis {text}';

    protected $description = 'Analyzes the frequency of runes in a given text.';

    public function handle(): int
    {
        $text = $this->argument('text');
        $runesOnly = preg_replace('/[^\x{16A0}-\x{16FF}]/u', '', $text);
        $totalRunes = mb_strlen($runesOnly);

        if ($totalRunes === 0) {
            $this->error('No runes found in the input text.');
            return self::FAILURE;
        }

        $frequencies = [];
        for ($i = 0; $i < $totalRunes; $i++) {
            $char = mb_substr($runesOnly, $i, 1);
            if (!isset($frequencies[$char])) {
                $frequencies[$char] = 0;
            }
            $frequencies[$char]++;
        }

        arsort($frequencies);

        $this->info("Total Runes: $totalRunes");
        $this->info("Rune Frequencies:");

        $headers = ['Rune', 'Count', 'Percentage', 'Gematria Index'];
        $data = [];

        foreach ($frequencies as $runeChar => $count) {
            $runeEnum = Rune::tryFrom($runeChar);
            $index = $runeEnum ? $runeEnum->toNumericPosition() : 'N/A';
            $percentage = number_format(($count / $totalRunes) * 100, 2) . '%';
            $data[] = [$runeChar, $count, $percentage, $index];
        }

        $this->table($headers, $data);

        // Calculate Index of Coincidence
        $ic = 0;
        foreach ($frequencies as $count) {
            $ic += $count * ($count - 1);
        }
        $ic = $ic / ($totalRunes * ($totalRunes - 1));

        $this->info("Index of Coincidence (normalized for 29 runes): " . number_format($ic * 29, 4));
        $this->info("Index of Coincidence (absolute): " . number_format($ic, 6));

        return self::SUCCESS;
    }
}
