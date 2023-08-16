#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
 int arr[]={4,8,10,14,-1,18,-8};
  int n=sizeof(arr)/sizeof(arr[0]);
  int k;
  cout<<"enter the kth element: ";
  cin>>k;
  std::sort(arr,arr+n);
  int min=arr[k-1];
  int max=arr[n-k];
  cout<<"max element: "<<max<<endl;
  cout<<"min element: "<<min<<endl;
  
    
}
