#include <bits/stdc++.h>
using namespace std;

int N;
vector<vector<string>> solutions;

bool isSafe(vector<string> &board, int row, int col) {

    for (int i = 0; i < row; i++)
        if (board[i][col] == 'Q') return false;

    for (int i = row-1, j = col-1; i >= 0 && j >= 0; i--, j--)
        if (board[i][j] == 'Q') return false;

   
    for (int i = row-1, j = col+1; i >= 0 && j < N; i--, j++)
        if (board[i][j] == 'Q') return false;

    return true;
}

void solve(int row, vector<string> &board) {
    if (row == N) {            
        solutions.push_back(board);
        return;
    }

    for (int col = 0; col < N; col++) {
        if (isSafe(board, row, col)) {
            board[row][col] = 'Q';   
            solve(row + 1, board);   
            board[row][col] = '_';  
        }
    }
}

int main() {
    cout << "Enter N: ";
    cin >> N;

    vector<string> board(N, string(N, '_'));
    solve(0, board);

    cout << "Total solutions: " << solutions.size() << "\n\n";
    for (auto &sol : solutions) {
        for (auto &row : sol) cout << row << "\n";
        cout << "\n";
    }
    return 0;
}
