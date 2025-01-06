// this solution does not work
#include <bits/stdc++.h>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int t;
	cin >> t;

	while (t--) {
		vector<long long> aa;
		map<long long, long long> counts;
		int n, k;

		cin >> n;
		cin >> k;
		long long a;
		for (long long i = 0; i < n; i++) {
			cin >> a;
			if (!counts[a]) {
				aa.push_back(a);
			}
			counts[a] += 1;
		}

		sort(aa.begin(), aa.end(), [&counts](const long long x, const long long y){
			return counts[x] < counts[y];
		});

		long long removed = 0;
		for (auto a : aa) {
			long long c = counts[a];
			if (k < c) {
				break;
			}

			k -= c;
			removed++;
		}

		if (counts.size() > removed) {
			cout << counts.size() - removed << "\n";
		} else {
			cout << 1 << "\n";
		}
	}

	return 0;
}
