def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1

    while i >= 0 and j >= 0:
        if nums2[j] >= nums1[i]:
            nums1[k] = nums2[j]
            j -= 1
        elif nums2[j] < nums1[i]:
            nums1[k] = nums1[i]
            i -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    print(nums1)


merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
merge([1], 1, [], 0)
merge([0], 0, [1], 1)
