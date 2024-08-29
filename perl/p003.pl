#!/usr/bin/env perl
use warnings;
use strict;

use Math::NumSeq::Primes;

use constant N => 600851475143;

my $seq = Math::NumSeq::Primes->new;
my $biggest_factor;
my $prime;

do {
    undef, $prime = $seq->next;
    $biggest_factor = $prime if N % $prime == 0;
} while ($prime < sqrt(N));

print "$biggest_factor\n";
