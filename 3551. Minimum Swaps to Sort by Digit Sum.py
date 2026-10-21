class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        
        def digit_sum(val: int) -> int:
            s = 0
            while val > 0:
                s += val % 10
                val //= 10
            return s
        
        
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        indexed_nums.sort(key=lambda item: (digit_sum(item[0]), item[0]))
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            
            if visited[i] or indexed_nums[i][1] == i:
                continue
            
            cycle_length = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
               
                curr = indexed_nums[curr][1]
                cycle_length += 1
            
            if cycle_length > 1:
                swaps += cycle_length - 1
                
        return swaps