from collections import deque

# on the callback add the nodes to the arr for topo sort
# but the arr is reverse of the topo sort

# to check id the graph cantain the cycle then just find
# topo sorting the the result will be wrong


# no cycle detection
def topoSortDFS(adj, N):
    vis = [False] * N
    ordering = []

    def dfs(node):
        vis[node] = True

        neis = adj[node]
        for nei in neis:
            if not vis[nei]:
                dfs(nei)

        # after recursion and during backtracking
        # add the ele to ordering
        ordering.append(node)

    for i in range(N):
        if not vis[i]:
            dfs(i)

    return list(reversed(ordering))


# TC - o(v+e)
def topoSortKahn(adj, N):
    indegree = [0] * N

    for i in range(N):
        for nei in adj[i]:
            indegree[nei] += 1

    q = deque()
    for i in range(N):
        if indegree[i] == 0:
            q.append(i)

    ordering = []

    while q:
        top = q.popleft()  # already have idg 0
        ordering.append(top)

        for nei in adj[top]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    if len(ordering) != N:
        # cyclic graph
        return None

    return list(reversed(ordering))
