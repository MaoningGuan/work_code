#include <bits/stdc++.h>

using namespace std;

const int maxn = 100000 + 10;
string c;
map<string, int>mp;

int main() {
#ifdef LOCAL
	freopen("input.in", "r", stdin);
#endif // LOCAL
	int n;
	while (~scanf("%d", &n)) {
		mp.clear();
		int ans = 0, p = 0;
		for (int i = 0; i < n; i++) {
			cin >> c;
			if (mp.count(c) == 0) {
				mp.insert(pair<string, int>(c, i));
			}
			else {
				int cnt = i - mp[c] + 1 - p;
				ans = ans > cnt ? ans : cnt;
				p += cnt;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}