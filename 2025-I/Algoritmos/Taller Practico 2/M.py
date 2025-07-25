import sys
from collections import deque

MOD = 10**9 + 7

def main():
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr += 1
    
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u = int(input[ptr])
        ptr += 1
        v = int(input[ptr])
        ptr += 1
        adj[u].append(v)
        adj[v].append(u)
    
    k = int(input[ptr])
    ptr += 1
    x = int(input[ptr])
    ptr += 1
    
    # Build tree with root at 1
    root = 1
    parent = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    q = deque([root])
    visited[root] = True
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                q.append(v)
    
    # Post-order traversal
    postord = []
    stack = [(root, False)]
    while stack:
        node, processed = stack.pop()
        if processed:
            postord.append(node)
            continue
        stack.append((node, True))
        for child in reversed(children[node]):
            stack.append((child, False))
    
    # Precompute type choices
    less_k_ways = k - 1
    greater_k_ways = (m - k) % MOD
    not_k_ways = (less_k_ways + greater_k_ways) % MOD
    
    # Initialize DP arrays
    dp_yes = [ [0] * (x + 1) for _ in range(n + 1) ]  # parent is type k
    dp_no = [ [0] * (x + 1) for _ in range(n + 1) ]   # parent is not type k
    
    for u in postord:
        # Compute dp_yes[u]: parent is type k, so u must be <k (not type k)
        curr_yes = [0] * (x + 1)
        curr_yes[0] = 1  # Empty product
        
        for child in children[u]:
            child_no = dp_no[child]
            temp = [0] * (x + 1)
            for i in range(x + 1):
                if curr_yes[i] == 0:
                    continue
                for j in range(x + 1 - i):
                    temp[i + j] = (temp[i + j] + curr_yes[i] * child_no[j]) % MOD
            curr_yes = temp
        
        if less_k_ways > 0:
            for t in range(x + 1):
                curr_yes[t] = (curr_yes[t] * less_k_ways) % MOD
        else:
            for t in range(x + 1):
                curr_yes[t] = 0
        
        dp_yes[u] = curr_yes
        
        # Compute dp_no[u]: parent is not type k
        curr_no = [0] * (x + 1)
        
        # Case 1: u is type k
        {
            temp_case = [0] * (x + 1)
            temp_case[0] = 1
            
            for child in children[u]:
                child_yes = dp_yes[child]
                temp = [0] * (x + 1)
                for i in range(x + 1):
                    if temp_case[i] == 0:
                        continue
                    for j in range(x + 1 - i):
                        temp[i + j] = (temp[i + j] + temp_case[i] * child_yes[j]) % MOD
                temp_case = temp
            
            for t in range(1, x + 1):
                if t - 1 >= 0 and temp_case[t - 1]:
                    curr_no[t] = (curr_no[t] + temp_case[t - 1]) % MOD
        }
        
        # Case 2: u is not type k
        {
            temp_case = [0] * (x + 1)
            temp_case[0] = 1
            
            for child in children[u]:
                child_no = dp_no[child]
                temp = [0] * (x + 1)
                for i in range(x + 1):
                    if temp_case[i] == 0:
                        continue
                    for j in range(x + 1 - i):
                        temp[i + j] = (temp[i + j] + temp_case[i] * child_no[j]) % MOD
                temp_case = temp
            
            if not_k_ways > 0:
                for t in range(x + 1):
                    temp_case[t] = (temp_case[t] * not_k_ways) % MOD
            else:
                for t in range(x + 1):
                    temp_case[t] = 0
            
            for t in range(x + 1):
                curr_no[t] = (curr_no[t] + temp_case[t]) % MOD
        }
        
        dp_no[u] = curr_no
    
    ans = sum(dp_no[root][t] for t in range(x + 1)) % MOD
    print(ans)

if __name__ == "__main__":
    main()