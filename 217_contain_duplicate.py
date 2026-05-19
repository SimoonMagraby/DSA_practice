def containsDuplicate(self, nums):
        seen = set() # Create an empty hash set
        for num in nums:
            if num in seen: # O(1) lookup time!
                return True
            seen.add(num) # O(1) insertion time
        return False