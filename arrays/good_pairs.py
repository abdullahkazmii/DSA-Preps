from typing import List


def good_pairs(nums: List[int]):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1

    return count


nums = [1, 2, 3, 1, 1, 3]
print(good_pairs(nums))  # Output: 4
