#include <iostream>

using namespace std;

int main()
{
    int rows;

    cout << "aqua man!,how many rows do u need ?" << endl;

    cin>>rows;

    for(int i=1;i<=rows;i++){

    cout<<endl;

    for(int j=1;j<=i;j++){

        cout<<"*";

    }
}

    return 0;
}
