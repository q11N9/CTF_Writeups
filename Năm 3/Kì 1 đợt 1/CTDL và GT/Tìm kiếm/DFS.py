from collections import deque

adj = [[] for _ in range(1001)]
visited = [False for _ in range(1001)]
def dfs(u : int):
    print(f"{u}", end=" ");
    visited[u] = True
    for i in adj[u]:
        if not visited[i]:
            dfs(i)

if __name__ == "__main__":
    n = int(input("Nhap n: "))
    m = int(input("Nhap m: "))
    for i in range(0, m):
        x = int(input("Nhap x: "))
        y = int(input("Nhap y: "))
        adj[x].append(y)
        adj[y].append(x)
    dfs(1)
