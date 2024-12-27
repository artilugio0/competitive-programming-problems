#include <iostream>
#include <cmath>

using namespace std;
int main() {
	int t;
	cin >> t;
	while (t--) {
		long long x;
		cin >> x;
		long long top = std::cbrt(x)+1;

		bool ok = false;
		for (long long a = 1; a < top; a++) {
			long long lo = 1;
			long long hi = top;
			long long a3 = std::pow(a, 3);

			while (lo + 1 < hi) {
				long long mid = (lo + hi)/2;
				if (std::pow(mid, 3) <= x - a3) {
       					lo = mid;
				} else {
					hi = mid;
				}
			}

			if (a3 + std::pow(lo, 3) == x) {
				cout << "YES\n";
				ok = true;
				break;
			}
		}

		if (!ok) {
			cout << "NO\n";
		}
	}
}
