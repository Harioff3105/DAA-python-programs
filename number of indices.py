def findIntersectionValues(nums1, nums2):
    answer1 = 0
    answer2 = 0

    for num in nums1:
        if num in nums2:
            answer1 += 1

    for num in nums2:
        if num in nums1:
            answer2 += 1

    return [answer1, answer2]

nums1 = [2, 3, 2]
nums2 = [1, 2]
print(findIntersectionValues(nums1, nums2))

nums1 = [4, 3, 2, 3, 1]
nums2 = [2, 2, 5, 2, 3, 6]
print(findIntersectionValues(nums1, nums2))