class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      output = [1 for i in range(len(nums))]  # Initialize output list with 1s

      # Calculate products of all elements to the left of each index
      for i in range(1, len(output)):
          output[i] = output[i-1] * nums[i-1]

      R = 1  # Initialize variable R with 1

      # Calculate products of all elements to the right of each index
      for i in range(len(output)-1, -1, -1):
          output[i] = output[i] * R  # Multiply the left product with the right product
          R *= nums[i]  # Update R by multiplying with the corresponding element

      return output  # Return the resulting output list
