#include <bits/stdc++.h>
using namespace std;
int rod_cut_bottomup(int p[], int n)
{
    if (n <= 0)
        return 0;
    int r[n + 1];
    r[0] = 0;
    for (int i = 1; i <= n; i++)
    {
        int q = INT_MIN;
        for (int j = 0; j < i; j++)
        {
            q = max(q, p[j] + r[i - j - 1]);
        }
        r[i] = q;
    }
    return r[n];
}
int rod_cut_topdown(int p[], int n, int r[])
{
    int q;
    if (n == 0)
        q = 0;
    else
        q = INT_MIN;
    for (int i = 1; i <= n; i++)
        q = max(q, p[i - 1] + rod_cut_topdown(p, n - i, r));
    r[n] = q;
    return q;
}
int memo_rod_cut(int p[], int n)
{
    if (n <= 0)
        return 0;
    int r[n + 1] = {INT_MIN};
    return rod_cut_topdown(p, n, r);
}

int main()
{
    int p[] = {1, 5, 8, 9, 10, 17, 17, 20, 24, 30};
    cout << "Maximum profit using Top-Down Approach:";
    cout << memo_rod_cut(p, sizeof(p) / sizeof(int));
    cout << "\nMaximum profit using Bottom-Up Approach:";
    cout << rod_cut_bottomup(p, sizeof(p) / sizeof(int));
    return 0;
}