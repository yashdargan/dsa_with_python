#include<iostream>
using namespace std;

int main()
{  int f=0;
  int arr[]={5,6,9,10,14,20};
  int n=sizeof(arr)/sizeof(arr[0]);
  cout<<"insert number"<<endl;
  cin>>f;
  for(int i=0;i<n;i++)
  { if(f==arr[i])
    {
      cout<<"the number founded at:"<<i;
      break;
    } 
  }
  return -1;
}

