#include<iostream.h>
using namespace std;
int main
{ int arr[]={1,2,3,4,5,6,7,8,10};
  int n=sizeof(arr)/sizeof(arr[0]);
  for(int i=0;i<n;i++)
  {
    if(arr[i]==i)
    {return arr[i];
    }
    return -1;
  }
return 0;
}
