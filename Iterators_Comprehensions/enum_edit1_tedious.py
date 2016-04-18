#!/usr/bin/env python

# Enuerates all possible words of edit distance 1 away from a given term
# given the specified alphabet.
#
# This version is very lengthy and could be made much tighter using
# list comprehensions.  You should be able to write a single line each for
# the assignments of splits, deletes, transposes, replaces and inserts
# 

def edits1(term, alphabet):
    splits     = []
    for i in range(len(term) + 1):
        splits.append((term[:i], term[i:]))

    deletes = []
    for a, b in splits:
        if b:
            deletes.append(a + b[1:])

    transposes = []
    for a, b in splits:
        if len(b)>1:
            transposes.append(a + b[1] + b[0] + b[2:])

    replaces = []
    for a, b in splits:
        for c in alphabet:
            if b:
                replaces.append(a + c + b[1:])

    inserts = []
    for a, b in splits:
        for c in alphabet:
            inserts.append(a + c + b)
    return set(deletes + transposes + replaces + inserts)

print("Enumeration of all possible variants of 'Hello' with a single change:")
print(edits1("Hello", set('abcdefghijklmnopqrstuvwxyz ')))

print()
print("Enumeration of all possible variants of 'ACCGAT' with a single change:")
print(edits1("ACCGAT", set('ACGT')))

