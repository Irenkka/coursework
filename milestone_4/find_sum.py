from typing import List, Tuple


#Time complexity: O(n^2)
#Space complexity: O(1)
def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    li_len = len(li)
    for i in range(li_len):
        left_over = target - li[i]
        for j in range(i+1,li_len):
            if li[j] == left_over:
                return (i, j)
            

#Time complexity: O(n)
#Space complexity: O(n)
def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    dictionary = {}
    length = len(li)
    for i in range(length):
        elem = li[i]
        diff = target - elem
        if diff in dictionary:
            return (i, dictionary[diff])
        dictionary[elem] = i


print(find_sum_fast(15, [1, 2, 3, 3, 7, 8]))