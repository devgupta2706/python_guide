#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int sum = 0, l = 1;
int path(int A[5][5], int n, int i, int j)
{
    if ((i == n - 1) && (j == n - 1))
        return sum;
    if ((i < n - 1) && (j < n - 1))
    {
        if (A[i][j + 1] > A[i + 1][j])
        {
            sum += A[i][j + 1];
            l++;
            A[i][j + 1] = 1;
            return path(A, n, i, j + 1);
        }
        else
        {
            sum += A[i + 1][j];
            l++;
            A[i + 1][j] = 1;
            return path(A, n, i + 1, j);
        }
    }
    else if (i == n - 1)
    {
        sum += A[i][j + 1];
        l++;
        A[i][j + 1] = 1;
        return path(A, n, i, j + 1);
    }
    else if (j == n - 1)
    {
        sum += A[i + 1][j];
        l++;
        A[i + 1][j] = 1;
        return path(A, n, i + 1, j);
    }
}
int main()
{
    int A[5][5], n;
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            A[i][j] = (i * j) % 7;
        }
    }
    for (int i = 0; i < 5; i++)
    {
        cout << "\n";
        for (int j = 0; j < 5; j++)
        {
            cout << A[i][j] << " ";
        }
    }
    cout << "\n"
         << path(A, 5, 0, 0) << " " << l;
    for (int i = 0; i < 5; i++)
    {
        cout << "\n";
        for (int j = 0; j < 5; j++)
        {
            cout << A[i][j] << " ";
        }
    }
    return 0;
}