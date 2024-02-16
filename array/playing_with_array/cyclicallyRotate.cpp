#include <algorithm>
#include <iostream>
using namespace std;

void reverse(int arr[],int s,int e)
{
for(int i=s,j=e;i<j;i++,j--)
    swap(arr[i],arr[j]);
}
int main()
{
  int arr[]={2,3,4,5,6,7,8};
  int n = sizeof(arr)/sizeof(arr[0]);
  int r;
  cout<<"enter the no . of rotation";
  cin>>r;
  reverse(arr,0,n-1);
  reverse(arr,0,r-1);
  reverse(arr,r,n-1);
  
  for(int i=0;i<n;i++)
  cout<<arr[i]<<" ";
}
