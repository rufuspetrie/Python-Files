
#include <iostream>
#include <vector>
#include <functional>
using namespace std;

using func = function<int(int)>;
auto add3 = [](int x){ return x+3; };
vector<int> map(vector<int> xs, func f);

int main(){
    vector<int> xs = {1, 2, 3, 4};
    vector<int> result = map(xs, add3);
    for(auto it=result.begin(); it!=result.end(); it++){
        cout << *it << " ";
    }
}

vector<int> map(vector<int> xs, func f){
    vector<int> result;
    for(auto it=xs.begin(); it!=xs.end(); it++){
        result.push_back(f(*it));
    }
    return result;
}
