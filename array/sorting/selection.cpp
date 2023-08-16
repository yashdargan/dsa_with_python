#include <future>
#include<iostream>
using namespace std;
int main()
{
  int arr[]={9,1,4,5,2,3,0};
  int n=sizeof(arr)/sizeof(arr[0]);

  for(int i=0;i<n-1;i++)
  {
    int min=i;
    for(int j=i+1;j<n;j++)
    {
      if(arr[min]>arr[j])
        min=j;
    }
    if(min!=i)
      swap(arr[min],arr[i]);
  }
  for(int i=0;i<n;i++)
    cout<<arr[i]<<" ";
}
