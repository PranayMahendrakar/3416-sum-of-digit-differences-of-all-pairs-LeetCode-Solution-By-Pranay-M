class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        # Convert all numbers to strings
        strs = [str(num) for num in nums]
        n = len(strs)
        m = len(strs[0])  # All numbers have same number of digits
        
        total = 0
        
        # For each digit position
        for pos in range(m):
            # Count occurrences of each digit at this position
            count = [0] * 10
            for s in strs:
                count[int(s[pos])] += 1
            
            # For each pair of different digits, add to total
            # Number of pairs with different digits = total pairs - pairs with same digit
            # Total pairs = n*(n-1)/2
            # Pairs with same digit = sum of count[d]*(count[d]-1)/2 for each digit d
            same_pairs = 0
            for c in count:
                same_pairs += c * (c - 1) // 2
            
            total_pairs = n * (n - 1) // 2
            total += total_pairs - same_pairs
        
        return total