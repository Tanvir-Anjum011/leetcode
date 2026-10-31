class Solution:
    def palindromePath(self, n: int, edges: list[list[int]],
                       s: str, queries: list[str]) -> list[bool]:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        value = [1 << (ord(c) - 97) for c in s]

        parent = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n

        prefix[0] = value[0]
        timer = 0
        stack = [0]

        while stack:
            u = stack.pop()

            if u < 0:
                tout[~u] = timer - 1
                continue

            tin[u] = timer
            timer += 1

            stack.append(~u)

            for v in graph[u]:
                if v == parent[u]:
                    continue

                parent[v] = u
                prefix[v] = prefix[u] ^ value[v]
                stack.append(v)

        LOG = n.bit_length()
        up = [parent]

        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[p] for p in prev])

        def lca(u, v):
            if tin[u] <= tin[v] <= tout[u]:
                return u

            if tin[v] <= tin[u] <= tout[v]:
                return v

            target = tin[v]

            for level in reversed(up):
                p = level[u]

                if not (tin[p] <= target <= tout[p]):
                    u = p

            return parent[u]

        bit = [0] * (n + 1)

        def add(i, x):
            i += 1

            while i <= n:
                bit[i] ^= x
                i += i & -i

        def get(i):
            result = 0
            i += 1

            while i:
                result ^= bit[i]
                i -= i & -i

            return result

        answer = []

        for q in queries:
            parts = q.split()
            u = int(parts[1])

            if parts[0] == "update":
                new = 1 << (ord(parts[2]) - 97)
                change = value[u] ^ new

                if change:
                    add(tin[u], change)

                    if tout[u] + 1 < n:
                        add(tout[u] + 1, change)

                    value[u] = new

            else:
                v = int(parts[2])
                p = lca(u, v)

                mask = prefix[u] ^ prefix[v] ^ value[p]
                mask ^= get(tin[u]) ^ get(tin[v])

                answer.append((mask & (mask - 1)) == 0)

        return answer