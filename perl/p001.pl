#!/usr/bin/env perl
use warnings;
use strict;

my $sum = 0;

for (my $i = 1; $i < 1000; $i++) {
    next if $i % 3 && $i % 5;
    $sum += $i
}

print "$sum\n";
