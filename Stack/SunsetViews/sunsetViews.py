# Given an array of buildings and a direction that all of the buildings face, return an array of the indices of the buildings that can see the sunset.
# A building can see the sunset if it's strictly taller than all of the buildings that come after it in the direction that it faces.
# The input array named buildings contains positive, non-zero integers representing the heights of the buildings. A building at indexi thus has a height denoted by buildings [i]. All of the buildings face the same direction, and this direction is either east or west, denoted by the input string named direction, which will always be equal to either "EAST" or "WEST". In relation to the input array, you can interpret these directions as right for east and left for west.
# Important note: the indices in the ouput array should be sorted in ascending order.

def sunsetViews(buildings, direction):
    # Write your code here.
    # Time - O(n)
    # Space - O(n)
    buildingsWithSunsetViews = []

    startIdx = 0 if direction == "WEST" else len(buildings) - 1
    step = 1 if direction == "WEST" else -1

    idx = startIdx
    runningMaxHeight = 0
    while idx >= 0 and idx < len(buildings):
        buildingHeight = buildings[idx]

        if buildingHeight > runningMaxHeight:
            runningMaxHeight = buildingHeight
            buildingsWithSunsetViews.append(idx)

        idx += step

    if direction == "EAST":
        return buildingsWithSunsetViews[::-1]
        
    return buildingsWithSunsetViews

# Stack solution
# def sunsetViews(buildings, direction):
#     # Write your code here.
#     # Time - O(n)
#     # Space - O(n)
#     output = []
    
#     if direction == "WEST":
#         maxStack = []
#         for i in range(len(buildings)):
#             print(maxStack)
#             if not maxStack:
#                 maxStack.append({'building': buildings[i], 'index': i})
#             if buildings[i] > maxStack[-1]['building']:
#                 maxStack.append({'building': buildings[i], 'index': i})
#             else:
#                 continue

#         while len(maxStack) > 0:
#             building = maxStack.pop()
#             output.append(building['index'])
#             # insert operation takes O(n) time so avoid using this method
#             # output.insert(0, building['index'])
            
#     else:
#         maxStack = []
#         for i in range(len(buildings) - 1, -1, -1):
#             print(maxStack)
#             if not maxStack:
#                 maxStack.append({'building': buildings[i], 'index': i})
#             if buildings[i] > maxStack[-1]['building']:
#                 maxStack.append({'building': buildings[i], 'index': i})
#             else:
#                 continue

#         while len(maxStack) > 0:
#             building = maxStack.pop()
#             output.append(building['index'])

#     if direction == "WEST":
#         # [::-1] slicing allows creating a new array in descreasing order
#         return output[::-1] 
        
#     return output