# include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;

		vector<long long> ai(n);
		for (int i=0; i<n; i++) cin >> ai[i];

		map<long long, vector<long long>> g;
		for (int i=1; i<n; i++) {
		    long long u = ai[i] + i;
		    long long v = u + i;
		    g[u].push_back(v);
		}

		// solve
		set<long long> vis;
		function<void(long long)> dfs = [&](long long u) -> void {
		    if (vis.count(u)) return;
		    vis.insert(u);
		    for (long long v : g[u]) dfs(v);
		};
		dfs(n);
		cout << *vis.rbegin() << "\n";
	}
}
