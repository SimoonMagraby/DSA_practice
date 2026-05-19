def twoSum(self, nums, target):
        seen_numbers = {}
    
        for current_index, num in enumerate(nums):
            complement = target - num
        
        # Check if the number we need was already visited
            if complement in seen_numbers:
            # Return the index of the complement and the current index
                return [seen_numbers[complement], current_index]
        
        # If not found, save the current number and its index for later
            seen_numbers[num] = current_index