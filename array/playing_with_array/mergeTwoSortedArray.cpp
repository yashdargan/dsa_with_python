#include <algorithm>
#include<iostream>
using namespace std;
int main()
{
  int n,m;
  cout<<"enter no. of element in arr1"<<endl;
  cin>>n;
  int arr1[n];
  cout<<"enter element in arr1:";
  for(int i=0;i<n;i++)
  {cin>>arr1[i];}
  cout<<"enter no. of element in arr2"<<endl;
  cin>>m;
  int arr2[m];
  cout<<"enter element in arr2:";
  for(int i=0;i<m;i++)
  {cin>>arr2[i];}
  int arr3[n+m];
  for(int i=0;i<n;i++)
  {
    arr3[i]=arr1[i];
  }
  for(int i=0;i<m;i++)
  {
    arr3[n+i]=arr2[i];
  }
  sort(arr3[0],arr3[n+m]);
  cout<<"here are sorted ones";
  for(int i=0;i<n+m;i++)
  {
    cout<<arr3[i];
  }
}
