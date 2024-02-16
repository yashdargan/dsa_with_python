#include <iostream>
#include <vector>
using namespace std;
int main()
{
  int arr1[]={2,4,6,7,8,10};
  int arr2[]={3,4,5,8,1,9,10};
  int n= sizeof(arr1)/sizeof(arr1[0]);
  int m = sizeof(arr2)/sizeof(arr2[0]);
  vector<int>arr3;
  vector<int>arr4;
   int i=0,j=0;
  while(i<n && j<m)
  {
    if(arr1[i]>arr2[j])
    {
      arr3.push_back(arr2[j]);
      j++;
    }
    else if(arr1[i]<arr2[j])
    {
      arr3.push_back(arr1[i]);
      i++;
    }
    else    {
      arr3.push_back(arr1[i]);
      arr4.push_back(arr1[i]);
      i++;
      j++;
    }
     }

  cout<<"union are"<<endl;
    for(int k=0;k<arr3.size();k++)
      cout<<arr3[k]<<" ";
cout<<endl;
  cout<<"intersection are"<<endl;
    for(int k=0;k<arr4.size();k++)
        cout<<arr4[k]<<" ";

}
