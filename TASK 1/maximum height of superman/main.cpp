#include <iostream>

using namespace std;

int main()
{   int n,Max=0;
    cout<<"how many heights did u recorded"<<endl;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];

    }
    for(int j=0;j<n;j++){
     if(arr[j]>Max){
        Max=arr[j];
     }
    }
    cout<<"the maximum height u recorded is "<<Max;
    return 0;
}
