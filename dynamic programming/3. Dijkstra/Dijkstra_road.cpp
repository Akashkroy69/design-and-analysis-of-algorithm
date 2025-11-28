#include <bits/stdc++.h>
using namespace std;

void dijkstra(vector<vector<pair<int,int>>> &graph, int src) {
    int V = graph.size();
    vector<int> dist(V, INT_MAX);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

    dist[src] = 0;
    pq.push({0, src});

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        for (auto &edge : graph[u]) {
            int v = edge.first;
            int weight = edge.second;

            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    cout << "\nShortest distances from node " << src << ":\n";
    for (int i = 0; i < V; i++)
        cout << "To " << i << " -- > " << dist[i] << endl;
}

int main() {
    int V, E;
    cout << "Enter number of junctions: ";
    cin >> V;
    cout << "Enter number of roads: ";
    cin >> E;

    vector<vector<pair<int,int>>> graph(V);
    cout << "Enter u v w (from u to v with cost w):\n";

    for (int i = 0; i < E; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back({v, w}); // directed road
    }

    int src;
    cout << "Enter source junction: ";
    cin >> src;

    dijkstra(graph, src);
    return 0;
}
