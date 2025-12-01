#include <iostream>
#include <vector>
using namespace std;

void insert(vector<int> &nums,int j){
    int key = nums[j];
    int i =j-1;
    while (i>=0 && nums[i]>key)
    {
        nums[i+1] = nums[i];
        i--;
    }
    nums[i+1] = key;
    
}

vector<int> insertionSort(vector<int> &nums,int lastIndex){

  
        
    if(lastIndex>0){
        insertionSort(nums,lastIndex-1);

        insert(nums,lastIndex);
    }


    return nums;


}

int main(){
    vector<int> nums = {9,6,0,3,1};
    insertionSort(nums,nums.size()-1);
    for(auto x : nums){
        cout<<x<<" ";
    }
}