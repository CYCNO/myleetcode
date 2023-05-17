class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # Dictionary to store the count of each number ({1: 3, 2: 2, 3: 1})
        freq = [[] for i in range(len(nums) + 1)]  # List of lists to store numbers grouped by their frequency ([[], [3], [2], [1], [], [], []])

        # Count the occurrences of each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Group numbers by their frequency
        for n, c in count.items():
            freq[c].append(n)

        res = []  # List to store the top k frequent numbers
        # Traverse the frequencies in descending order
        for i in range(len(freq) - 1, 0, -1):
            # Traverse the numbers with the current frequency
            for n in freq[i]:
                res.append(n)  # Add the number to the result
                if len(res) == k:  # If we have found the top k frequent numbers, return the result
                    return res # [1, 2]
