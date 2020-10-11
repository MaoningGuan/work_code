//#include <bits/stdc++.h>
//
//using namespace std;
//
//const int maxn = 100010 * 2;
//
//long long A[maxn], pre_sum[maxn];
//
//int main() {
//#ifdef LOCAL
//	freopen("input.in", "r", stdin);
//#endif // LOCAL
//	int T;
//
//	while (~scanf("%d", &T)) {
//		while (T--) {
//			int N = 0;
//			scanf("%d", &N);
//			for (int i = 0; i < N; i++) {
//				scanf("%lld", &A[i]);
//				A[i + N] = A[i];
//			}
//			pre_sum[0] = A[0];
//			for (int i = 1; i < 2 * N; i++)
//				pre_sum[i] = pre_sum[i - 1] + A[i];
//			long long sum = 0, ans = A[0];
//			int p = 0;
//			for (int i = 0; i < 2 * N; i++) {
//				if (sum < 0) {
//					sum = 0;
//					p = i;
//				}
//				if (i - p + 1 > N) {
//					p++;
//					while (A[p] < 0 && p < N - 1)
//						p++;
//					i = N;
//					sum = sum - pre_sum[p-1];
//
//				}
//				sum += A[i];
//				ans = ans > sum ? ans : sum;
//				if (p >= N)
//					break;
//
//			}
//			if (ans < 0)
//				ans = 0;
//			printf("%lld\n", ans);
//
//		}
//	}
//	return 0;
//}