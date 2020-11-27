#!/usr/bin/env python3
import sys
import heapq as hq
import math

# this TLEs

def send_email(graph, weights, source, target):
    pq = [(0, source)]
    n = len(graph)
    visited = set()
    dist = [float('inf') for _ in range(n)]
    dist[source] = 0
    while pq:
        w, curr_node = hq.heappop(pq)
        visited.add(curr_node)
        for node in graph[curr_node]:
            if node not in visited:
                w = weights[curr_node][node]
                if dist[node] > w+dist[curr_node]:
                    dist[node] = w+dist[curr_node]
                    hq.heappush(pq, (dist[node], node))
                    
    if math.isinf(dist[target]):
        return 'unreachable'

    return dist[target]





if __name__ == "__main__":
    lines = iter(sys.stdin.readlines())
    ncases=int(next(lines))

    for i in range(ncases):
        n, m, S, T = next(lines).split()
        n = int(n)
        m = int(m)
        S = int(S)
        T = int(T)
        graph = [[]]*int(n)
        weights = [[-1 for i in range(n)] for j in range(n)]
        source_node = int(S)
        target_node = int(T)
        m = int(m)
        j = i
        for i in range(m):
            s1, s2, w = next(lines).split()
            s1 = int(s1)
            s2 = int(s2)
            w = int(w)
            graph[s1].append(s2)
            graph[s2].append(s1)
            weights[s1][s2] = w
            weights[s2][s1] = w
        mills = send_email(graph, weights, source_node, target_node)
        # ret = send_network_x(g, source_node, target_node)
        print('Case #{}: {}'.format(j+1, mills))
