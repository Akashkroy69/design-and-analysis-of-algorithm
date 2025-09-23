#include <iostream>
#include <vector>
using namespace std;

int count = 0;
int fib(int n, vector<int> &dp){
    count++;
    if (n==0) return 0;
    if (n==1) return 1;

    // this memoization logic is added to reduce the time complexity from exponential to linear
    if(dp[n]!=-1) return dp[n];

    return dp[n] = fib(n-1,dp) + fib(n-2,dp);


}

int main(){

    int n;
    cout<<"enter a value for n: \n";
    cin>>n;
    vector<int> dp(max(2, n), -1); // Ensure size at least 2
    dp[0] = 0;
    dp[1] = 1;
    cout<<"fib value for "<<n<<" is "<<fib(n,dp)<<endl;
    cout<<"count value is "<<count<<endl;
}