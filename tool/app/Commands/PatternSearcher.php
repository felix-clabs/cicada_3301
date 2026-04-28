<?php

namespace App\Commands;

use App\Enums\Rune;
use Illuminate\Support\Str;
use LaravelZero\Framework\Commands\Command;

class PatternSearcher extends Command
{
    protected $signature = 'app:pattern-searcher {text} {--word=}';

    protected $description = 'Searches for common Cicada patterns or a specific word using different Gematria variations.';

    public function handle(): int
    {
        $text = $this->argument('text');
        $word = $this->option('word') ?? 'CICADA';

        $this->info("Searching for patterns related to: $word");

        // Convert word to runes
        $wordRunes = '';
        foreach (str_split(strtoupper($word)) as $char) {
            $rune = Rune::tryFromEnglish($char);
            if ($rune) {
                $wordRunes .= $rune->toRune();
            }
        }

        if (empty($wordRunes)) {
            $this->error("Could not convert $word to runes.");
            return self::FAILURE;
        }

        $this->info("Word in Runes: $wordRunes");

        // Simple search
        if (Str::contains($text, $wordRunes)) {
            $this->success("Exact pattern found!");
        } else {
            $this->warn("Exact pattern not found. Attempting fuzzy/shift search...");
        }

        // TODO: Implement Caesar shift search on the word runes
        for ($shift = 1; $shift < 29; $shift++) {
            $shiftedWord = '';
            for ($i = 0; $i < mb_strlen($wordRunes); $i++) {
                $char = mb_substr($wordRunes, $i, 1);
                $rune = Rune::tryFrom($char);
                $newPos = ($rune->toNumericPosition() + $shift) % 29;
                $shiftedWord .= Rune::tryFromIndex($newPos)->toRune();
            }

            if (Str::contains($text, $shiftedWord)) {
                $this->info("Pattern found with shift $shift: $shiftedWord");
            }
        }

        return self::SUCCESS;
    }
}
