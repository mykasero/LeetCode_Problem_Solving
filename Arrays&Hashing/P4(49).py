# LeetCode Problem Name: Group Anagrams
strs = ["eat","tea","tan","ate","nat","bat"] #Example list

letters = {}

for s in strs:
    sorter = ''.join(sorted(s))
    if sorter not in letters:
        letters[sorter] = [s]
    else:
        letters[sorter].append(s)

return list(letters.values())
    
