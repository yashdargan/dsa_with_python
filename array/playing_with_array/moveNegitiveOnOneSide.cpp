#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
  int arr[]={1,-1,3,5,-9,10,-10,-11,12,30,40};
  int n = sizeof(arr)/sizeof(arr[0]);

std::sort(arr,arr+n);

  for(int i=0;i<n;i++)
  cout<<arr[i]<<" ";
}
