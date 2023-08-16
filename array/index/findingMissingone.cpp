#include <iostream>
using namespace std;
int main()
{
  int arr[]={1,2,3,4,5,6,7,8,10};
  int n= sizeof(arr)/sizeof(arr[0]);
  for(int i=1;i<=n;i++)
  {
    if(arr[i-1]!=i)
      cout<<i;
  }
  return -1;
}
