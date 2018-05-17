#!/usr/bin/env python3

s = 'CAATCCAAC'  # example sequence
k = 3  # kmer length

l = [] # initialize empty list
for i in range(0, len(s)):
    if i+k < len(s):
        tmp = [s[i:i+k]]
        l.append(tmp)
