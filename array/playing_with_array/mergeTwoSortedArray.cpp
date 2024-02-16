#include <algorithm>
#include<iostream>
#include<vector>
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
//space complexity = O(n)
 /*
  int arr3[n+m];

  int left=0,right=0,index=0;
  while(left<n && right<m)
  {
     if(arr1[left]>=arr2[right])
    {
       arr3[index]=arr2[right];
      index++;right++;
    }
    else{
      arr3[index]=arr1[left];
      index++;left++;
    }
  }
  while(left<n)
    arr3[index++]=arr1[left++];
  while(right<m)
    arr3[index++]=arr2[right++];


for(int i=0;i<n+m;i++){
    if(i<n)
    {arr1[i]=arr3[i];
     cout<<arr1[i]<<" "; }
    else
    {arr2[i-n]=arr3[i];
    cout<<arr2[i-n]<<" ";
    }
  }
 */ 
// space complexity = O(1)
  int left =n-1, right =0;
  while(left>=0 && right<m)
  {
    if(arr1[left]>arr2[right])
    {swap(arr1[left],arr2[right]);
      left--;right++;}
    else {
      break;
    }
  }
  sort(arr1,arr1+n);
  sort(arr2,arr2+m);

  for(int i=0;i<n+m;i++)
  { if(i<n)
    cout<<arr1[i]<<" ";
      else 
    cout<<arr2[i-n]<<" ";
  }
}
