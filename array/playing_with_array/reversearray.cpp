#include <iostream>
using namespace std;
int main()
{
  int arr[]={2,4,5,8,10};
  int n=sizeof(arr)/sizeof(arr[0]);
  int *ftr=&arr[0];
  int *btr=&arr[n-1];
  int a=n/2;
  while(a--)
  {
    int t= *ftr;
    *ftr=*btr;
    *btr=t;
    ftr++;
    btr--;

  }

  for(int i=0;i<n;i++)
  {
    cout<<arr[i]<<" ";
  }

}
