
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right):
            if left <= start and end <= right:
                old_sum = tree[node]
                tree[node] += end - start + 1
                lazy[node] += 1
                return old_sum

            mid = (start + end) // 2

            if lazy[node]:
                val = lazy[node]
                l, r = node * 2, node * 2 + 1

                tree[l] += val * (mid - start + 1)
                tree[r] += val * (end - mid)

                lazy[l] += val
                lazy[r] += val
                lazy[node] = 0

            old_sum = 0

            if left <= mid:
                old_sum += update(
                    node * 2, start, mid, left, right
                )

            if right > mid:
                old_sum += update(
                    node * 2 + 1, mid + 1, end, left, right
                )

            tree[node] = tree[node * 2] + tree[node * 2 + 1]
            return old_sum

        last_seen = {}
        current_sum = 0
        answer = 0

        for i, num in enumerate(nums):
            left = last_seen.get(num, -1) + 1

            old_sum = update(1, 0, n - 1, left, i)

            current_sum = (
                current_sum + 2 * old_sum + (i - left + 1)
            ) % MOD

            answer = (answer + current_sum) % MOD

            last_seen[num] = i

        return answer
