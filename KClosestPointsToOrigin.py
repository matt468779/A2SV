from cmath import inf
from typing import List
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    lengths = []
    result = []*k
    for i in range(len(points)):
        lengths.append([pow(points[i][0],2)+pow(points[i][1], 2), i])
    lengths = mergeSort(lengths)

    for i in range(k):
        result.append(points[lengths[i][1]])
    return result

def mergeSort(arr: List[List]):
    if len(arr) > 1:
        l = mergeSort(arr[0: len(arr)//2])
        r = mergeSort(arr[len(arr)//2: len(arr)])
        return merge(l, r)
    else:
        return arr

def merge(l: List[List], r: List[List]):
    merged = []
    i = 0
    l.append([inf, -1])
    r.append([inf, -1])
    lIndex = 0
    rIndex = 0
    while i < len(l) + len(r) - 2:
        if l[lIndex][0] < r[rIndex][0]:
            merged.append(l[lIndex])
            lIndex += 1
        else:
            merged.append(r[rIndex])
            rIndex += 1
        i+=1
    return merged



if __name__ == "__main__":
    arr = [5,4,3,2,1]
    points = [[68,97],[34,-84],[60,100],[2,31],[-27,-38],[-73,-74],[-55,-39],[62,91],[62,92],[-57,-67]]
    print(kClosest(points, 5))