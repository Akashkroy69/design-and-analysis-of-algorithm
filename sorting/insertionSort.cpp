#include <iostream>
#include <vector>
using namespace std;

vector<int> insertionSort(vector<int> &nums){
// [9.6.0,3,1]
    for(int j=1;j<nums.size();j++){
        int key = nums[j];
        int i = j-1;
        while(i>=0 && nums[i] > key){
            nums[i+1] = nums[i];
            i--;

        }
        nums[i+1] = key;
    }
    for(auto x: nums){
        cout<<x<<" ";
    }
    cout<<endl;
    return nums;


}

int main(){
    vector<int> nums = {9,6,0,3,1};
    insertionSort(nums);
}