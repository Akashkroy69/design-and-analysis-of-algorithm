#include <iostream>

using namespace std;
int count =0;
int fib(int num){
    count++;
    if (num == 0) return 0;
    if (num == 1) return 1;

    return fib(num -1 ) + fib(num-2);

}

int main(){


    for(int x = 0; x<=10;x++)
        cout<<"fib for "<<x<<" : "<<fib(x)<<endl;
        cout<<"count value "<<count<<endl;
}

// time complexity : 2^n
// space complexity: n