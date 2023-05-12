import heapq
nums = [1,1,1,2,2,3]
k = 2

counted_vals = {}
heap = []
max_freq = []
heapq.heapify(heap)

for num in nums:
    if num in counted_vals:
        counted_vals[num] += 1
    else:
        counted_vals[num] = 1

for key,value in counted_vals.items():
    heapq.heappush(heap,(-value,key))


while heap and len(max_freq)<k:
    max_freq.append(heapq.heappop(heap)[1])

# print(max_freq)
print(counted_vals.items())

