a = [1,23,28,12,16,18,17,11,15,12,22,91,42,152]
result = []

# for i in a:
#     print(i)
def findmin(data):
    minval = data[0]
    for i in range(len(data)-1):
        if data[i] < minval:
            minval = data[i]
    return minval


while len(a) > 0:
    for i in a:
        less_than = findmin(a)
        result.append(less_than)
        a.remove(less_than)
print(result)