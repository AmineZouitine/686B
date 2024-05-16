
# def distance(i, j):
#     return abs(i, j)


# def findPath(current_index, target_index, shortCuts, currentDistance, alreadyVisited = []):
#     if current_index == target_index:
#         return currentDistance
    
#     if current_index in alreadyVisited:
#         return 1000000
    
#     alreadyVisited.append(current_index)

#     return min(
#         findPath(current_index + 1, target_index, shortCuts, currentDistance + 1),
#         findPath(shortCuts[current_index], target_index, shortCuts, currentDistance + 1))



def bfs(shortCuts):
    maxSize = len(shortCuts)
    mins = [float('inf')] * maxSize
    mins[0] = 0
    queue = [(0, 0)]
    
    while len(queue) != 0:
        current_index, current_energy = queue.pop(0)
        
        if current_index + 1 < maxSize and current_energy + 1 < mins[current_index + 1]:
            mins[current_index + 1] = current_energy + 1
            queue.append((current_index + 1, current_energy + 1))
        
        shortcut_index = shortCuts[current_index] - 1
        if current_energy + 1 < mins[shortcut_index]:
            mins[shortcut_index] = current_energy + 1
            queue.append((shortcut_index, current_energy + 1))
    
    return mins

# 3
# 2 2 3

# print(findPath(0, 2, [2, 2, 3], 0))
# print(findPath(0, 1, [2, 2, 3], 0))

_ = input()
shortCuts = list(map(int, input().split()))
print(bfs(shortCuts))
