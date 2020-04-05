The code is in C++
#include <bits/stdc++.h>

using namespace std;

int s[60][60], no, ac, t;
bool row_s[60][60], col_s[60][60], solve;

void sol(int row, int col, int m) {
    if (row == no && col == no + 1 && m == ac && !solve) {
        solve = true;
        cout << "Case #" << t << ": " << "POSSIBLE\n";
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                cout << s[i][j] << " ";
            }
            cout << "\n";
        }
        return;
    } else if (row > n) {
        return;
    } else if (col > n) {
        solver(row + 1, 1, m);
    }
    for (int i = 1; i <= n && !solve; ++i) {
        if (!row_s[row][i] && !col_s[col][i]) {
            row_s[row][i] = col_s[col][i] = true;
            if (row == col) {
                m += i;
            }
            s[row][col] = i;

            sol(row, col + 1, m);

            row_s[row][i] = col_s[col][i] = false;
            if (row == col) {
                m -= i;
            }
            s[row][col] = 0;
        }
    }
}

int main() {
    int Test;
    scanf(" %d", &Test);
    for (t = 1; t <= Test; ++t) {
        scanf(" %d %d", &no, &ac);
        sol(1, 1, 0);
        if (!solve) {
            cout << "Case #" << t << ": " << "IMPOSSIBLE\n";
        }
        solve = false;
    }
    return 0;
}
    