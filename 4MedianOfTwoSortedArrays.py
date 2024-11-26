from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = []
        all_size = len(nums1) + len(nums2)
        half_size = all_size // 2 
        i = 0
        j = 0

        # Create array temp
        while len(temp) < half_size + 1:
            if i >= len(nums1):  # out of range i
                temp.append(nums2[j]) 
                j += 1
            elif j >= len(nums2):  # out of range j
                temp.append(nums1[i])
                i += 1
            else:  # no out of range
                if nums1[i] <= nums2[j]: 
                    temp.append(nums1[i])
                    i += 1
                else:
                    temp.append(nums2[j])
                    j += 1

        # Find median
        if all_size % 2 == 0:  # even size
            return (temp[-2] + temp[-1]) / 2
        else:  # odd size
            return float(temp[-1])
