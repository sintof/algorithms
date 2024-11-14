#include <bits/stdc++.h>
using namespace std;


void dfs_adj_recursively(int u, vector<vector<int>> &adj, vector<int> &visited){
    visited[u] = 1;

    for(int i = 0; i < adj[u].size(); i++){
        if(visited[adj[u][i]] == 0){
            dfs_adj_recursively(adj[u][i], adj, visited);
        }
    }

    cout << u << " ";
}


void bfs(int u, vector<vector<int>> &adj){
    vector<bool> visited(adj.size(), false);
    queue<int> q;
    q.push(u);
    visited[u] = true;
    while(!q.empty()){
        u = q.front();
        q.pop();

        for(int v : adj[u]){
            if(!visited[v]){
                q.push(v);
                visited[v] = true;
                cout << v << " ";
            }
        }
    }
}



int main()
{
    cout << "Hello World!" << endl;
    return 0;
}