#include <iostream>
using namespace std;
int main()
{
  int arr[]={4,6,9,13,15,20,25,32,84};
  int n= sizeof(arr)/sizeof(arr[0]);
  cout<<"enter the numberv to find in sorted array:";
  int find;
  cin>>find;
  for(int i=0;i<n;i++)
  { 
    if(find==arr[i])
      cout<<i;
  }
  return -1;
}
