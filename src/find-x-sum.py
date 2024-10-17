from collections import Counter
from heapq import nlargest


def find_x_sum(nums: list[int], k: int, x: int) -> list[int]:
    n = len(nums)
    result = []

    # Step 1: Initialize the sliding window and the frequency counter
    freq = Counter(nums[:k])
    print(freq)

    # Step 2: Function to calculate the x-sum of the current window
    def calculate_x_sum(freq):
        # Get the top x elements based on frequency and then value
        top_x = nlargest(x, freq.items(), key=lambda pair: (pair[1], pair[0]))
        print(top_x)
        return sum([elem * count for elem, count in top_x])


    # Step 3: Calculate the x-sum for the first window
    result.append(calculate_x_sum(freq))
    print(result)

    # Step 4: Slide the window from index 1 to n - k
    for i in range(1, n - k + 1):
        # Remove the element that goes out of the window
        left_elem = nums[i - 1]
        freq[left_elem] -= 1
        if freq[left_elem] == 0:
            del freq[left_elem]

        # Add the new element that comes into the window
        right_elem = nums[i + k - 1]
        freq[right_elem] += 1

        # Calculate the x-sum for the current window
        result.append(calculate_x_sum(freq))

    print(result)
    return result


find_x_sum([1, 1, 2, 2, 3, 4, 2, 3], 6, 2)  # [6,10,12]
# find_x_sum([3, 8, 7, 8, 7, 5], 2, 2)  # [11,15,15,15,12]
