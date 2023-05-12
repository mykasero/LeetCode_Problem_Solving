## LeetCode Problem Name: Valid Anagram
s = "aacc" #example string
t = "ccac" #example string
'''
#original idea (passed 33/38)

count=0

for i in s:
    if i in t:
        count+=1
    
if count == len(s):
    print(True)
else:
    print(False)
'''
# fully passed idea

if len(s) != len(t):
    print(False)
for i in set(s):
    # Compare s.count(l) and t.count(l) for every index i from 0 to 26...
    # If they are different, return false...
    print("s count: ",s.count(i),'| t count: ',t.count(i))
    # if s.count(i) != t.count(i):
    #     print(False)
print(True)       

