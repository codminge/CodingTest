def solution(spell, dic):
    spellCounts = get_counts(spell)
    for i in dic:
        dicCounts = get_counts(i)
        if dicCounts == spellCounts:
            return 1
    return 2

def get_counts(seq):
    counts = {}
    for x in seq:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts