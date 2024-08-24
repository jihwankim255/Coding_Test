#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

const int MAX_N = 100001;

int n;
vector<int> adj[MAX_N];
int parent[MAX_N];
int l[MAX_N], r[MAX_N];
set<int> subtrees[MAX_N];

bool isAdjacent(int u, int v, bool visited[]);
bool dfs(int u, int v, bool visited[]);

bool isIntervalGraph() {
    // 트리의 모든 리프 노드를 찾는다.
    vector<int> leaves;
    for (int i = 1; i <= n; i++) {
        if (adj[i].size() == 1) {
            leaves.push_back(i);
        }
    }

    // 리프 노드가 없는 경우, 트리가 구간 그래프가 아니다.
    if (leaves.empty()) {
        return false;
    }

    // 리프 노드부터 시작하여, 각 정점의 구간을 위에서 아래로 순서대로 계산한다.
    for (int leaf : leaves) {
        l[leaf] = 0;
        r[leaf] = 1;
        subtrees[leaf].insert(leaf);
    }

    for (int i = n - 1; i >= 1; i--) {
        int u = adj[i][0];
        int v = i;

        // 자식 노드의 구간을 이용하여 부모 노드의 구간을 계산한다.
        if (l[u] > r[u]) {
            swap(l[u], r[u]);
        }
        l[v] = r[u];
        r[v] = l[u] + r[u];

        // 자식 노드의 서브트리 정보를 부모 노드의 서브트리 정보에 병합한다.
        subtrees[v].insert(subtrees[u].begin(), subtrees[u].end());

        // 부모 노드와 자식 노드가 같은 서브트리에 속하지 않는 경우,
        // 트리가 구간 그래프가 아니다.
        for (int subtree : subtrees[u]) {
            if (!subtrees[v].count(subtree)) {
                return false;
            }
        }
    }

    return true;
}

void printIntervals() {
    for (int i = 1; i <= n; i++) {
        cout << l[i] << " " << r[i] * 2 << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for (int i = 1; i < n; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        parent[v] = u;
    }

    // 이미지에 제시된 조건을 추가합니다.
    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            if (parent[i] == parent[j]) {
                // 두 정점이 같은 부모를 가지고 있고, 서로 연결되어 있지 않은 경우,
                // 트리가 구간 그래프가 아니다.
                bool visited[MAX_N] = {false}; // visited 배열 초기화
                if (!isAdjacent(i, j, visited)) {
                    cout << -1 << "\n";
                    return 0;
                }
            }
        }
    }

    if (!isIntervalGraph()) {
        cout << -1 << "\n";
        return 0;
    }

    cout << 1 << "\n";
    printIntervals();

    return 0;
}

bool isAdjacent(int u, int v, bool visited[]) {
    // 두 정점이 같은 경로에 있는지 확인합니다.
    return dfs(u, v, visited);
}

bool dfs(int u, int v, bool visited[]) {
    visited[u] = true;
    if (u == v) {
        return true;
    }
    for (int neighbor : adj[u]) {
        if (!visited[neighbor] && dfs(neighbor, v, visited)) {
            return true;
        }
    }
    return false;
}
