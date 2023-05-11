strs = ["eat","tea","tan","ate","nat","bat"]

letters = {}

for s in strs:
    sorter = ''.join(sorted(s))
    if sorter not in letters:
        letters[sorter] = [s]
    else:
        letters[sorter].append(s)

return list(letters.values())
    
