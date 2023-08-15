notes = 'до, ре, ми, фа, соль, ля, си'.split(', ')
print(*sorted(input().split(), key=notes.index))
