#include<iostream>
using namespace std;
int main()
{
  int arr[]={20,-10,30,-40,100};
  int n=sizeof(arr)/sizeof(arr[0]);
  int min=arr[0];
  int max=arr[0];
  for(int i=0;i<n;i++)
  {
    if(min>arr[i])
       min=arr[i];
    if(max<arr[i])
      max=arr[i];
  }
cout<<"mininmum is :"<<min<<endl;
cout<<"maximum is:"<<max<<endl;  

}
