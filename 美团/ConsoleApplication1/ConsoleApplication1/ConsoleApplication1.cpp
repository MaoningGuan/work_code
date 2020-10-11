//#include <bits/stdc++.h>
//
//using namespace std;
//
//const int maxn = 10000010;
//int a[maxn];
//
//bool cmp(int a, int b) {
//	return a > b;
//}
//
//int main() {
//#ifdef LOCAL
//	freopen("input.in", "r", stdin);
//#endif // LOCAL
//	int n, x;
//	while (~scanf("%d%d", &n, &x)) {
//		for (int i = 1; i <= n; i++) {
//			scanf("%d", &a[i]);
//		}
//		sort(a + 1, a + n + 1, cmp);
//		int ans = x;
//		if (a[x] == 0) {
//			for (int i = x; i >= 1; i--) {
//				if (a[i] > 0) {
//					break;
//				}
//				ans--;
//			}
//		}
//		else
//		{
//			for (int i = x + 1; i <= n; i++) {
//				if (a[i] != a[x]) {
//					break;
//				}
//				ans++;
//			}
//		}
//		printf("%d\n", ans);
//	}
//	return 0;
//}