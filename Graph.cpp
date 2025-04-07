#include "Graph.hpp"
#include <vector>
#include <queue>
#include <unordered_map>
#include <limits>
#include <algorithm> // for std::reverse

// Graph member functions
void Graph::addEdge(int from, int to, int weight) {
    adjList[from].push_back({to, weight});
    adjList[to].push_back({from, weight}); // undirected graph
}

std::vector<int> Graph::dijkstra(int start, int goal) {
    std::unordered_map<int, int> dist;
    std::unordered_map<int, int> prev;

    for (auto& node : adjList) {
        dist[node.first] = std::numeric_limits<int>::max();
    }
    dist[start] = 0;

    using pii = std::pair<int, int>;
    std::priority_queue<pii, std::vector<pii>, std::greater<pii>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        int current = pq.top().second;
        pq.pop();

        if (current == goal) break;

        for (auto& neighbor : adjList[current]) {
            int newDist = dist[current] + neighbor.weight;
            if (newDist < dist[neighbor.to]) {
                dist[neighbor.to] = newDist;
                prev[neighbor.to] = current;
                pq.push({newDist, neighbor.to});
            }
        }
    }

    std::vector<int> path;
    for (int at = goal; at != start; at = prev[at]) {
        path.push_back(at);
    }
    path.push_back(start);
    std::reverse(path.begin(), path.end());
    return path;
}
