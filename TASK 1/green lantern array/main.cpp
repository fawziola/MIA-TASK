#include <iostream>

using namespace std;

int main()
{
   bool flag=0;
   int n,elements,ele;
   cout<<"how many elements do u want to check"<<endl;
   cin>>n;
   int arr[n];


   cout<<"enter your elements"<<endl;
   for(int i=0;i<n;i++)
   {
    cin>>elements;
    arr[i]=elements;
   }
   cout<<"which element do u want to check"<<endl;
   cin>>ele;
   for(int j=0;j<n;j++){
    if (arr[j]==ele){
        cout<<j;
        flag=true;
        break;
    }
   }
   if(!flag){
        cout<<"-1";

   }
    return 0;
}
