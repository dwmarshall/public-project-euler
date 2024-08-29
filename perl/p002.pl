#!/usr/bin/env perl
use warnings;
use strict;

my $f1 = 1;
my $f2 = 2;
my $f3 = 3;

my $sum = 2;

while ($f3 < 4_000_000) {
    if ($f3 % 2 == 0) {
        $sum += $f3
    }
    $f1 = $f2;
    $f2 = $f3;
    $f3 = $f1 + $f2
}

print "$sum\n";
