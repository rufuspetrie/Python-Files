
#include <iostream>
using namespace std;

int lazyfib(int n);

int main(){
    cout << lazyfib(10);
}

int lazyfib(int n){
    if((n==1) or (n==2)){
        return 1;
    }
    else{
        return lazyfib(n-1) + lazyfib(n-2);
    }
}
