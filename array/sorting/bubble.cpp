#include <future>
#include<iostream>
#include <algorithm>
using namespace std;
int main()
{
  int arr[]={9,1,4,5,2,3,0};
  int n = sizeof(arr)/sizeof(arr[0]);
  for(int i=0;i<n-1;i++)
  {
    int flag=0;
    for(int j=0;j<n-1-i;j++)
    {
      if(arr[j]>arr[j+1])
      {
        swap(arr[j],arr[j+1]);
        flag=1;
      }
    }
    if(flag==0)
      break;
  }
  for(int i=0;i<n;i++)
  cout<<arr[i]<<" ";
}
