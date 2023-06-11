#include <iostream>
using namespace std;

int N, L;
int map[100][100];

bool check_row(int row) {
    int cur_height = map[row][0];
    int cnt = 1;

    for (int col = 1; col < N; col++) {
        if (map[row][col] == cur_height) {
            cnt++;
        } else if (map[row][col] == cur_height + 1 && cnt >= L) {
            cnt = 1;
            cur_height++;
        } else if (map[row][col] == cur_height - 1 && cnt >= 0) {
            cnt = -L + 1;
            cur_height--;
        } else {
            return false;
        }
    }

    return cnt >= 0;
}

bool check_col(int col) {
    int cur_height = map[0][col];
    int cnt = 1;

    for (int row = 1; row < N; row++) {
        if (map[row][col] == cur_height) {
            cnt++;
        } else if (map[row][col] == cur_height + 1 && cnt >= L) {
            cnt = 1;
            cur_height++;
        } else if (map[row][col] == cur_height - 1 && cnt >= 0) {
            cnt = -L + 1;
            cur_height--;
        } else {
          return false;
        }
    }

    return cnt >= 0;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> L;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> map[i][j];

    int ans = 0;
    for (int i = 0; i < N; i++) {
        if (check_row(i)) ans++;
        if (check_col(i)) ans++;
    }

    cout << ans << endl;

    return 0;
}
