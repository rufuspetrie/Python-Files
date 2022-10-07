
#include <iostream>
#include <vector>
#include <numeric>
#include <iomanip>
#include <cmath>
#include <functional>
using std::vector;
using std::cout;
using std::function;
using func = function<double(double)>;

double newton(double x0, func f, func grad, int max_iter=100){
    double x = x0;
    for(int i=0; i<max_iter; i++){
        x -= f(x)/grad(x);
    }
    return x;
}

int main(){
    auto f = [](double x){return pow(x,3) - 7*x - 6;};
    auto grad = [](double x){return 3.0*pow(x,2) - 7;};
    vector<double> x = {-5, 0, 5};
    for(auto& x0: x){
        cout << std::setw(2) << x0 << ": " << std::setw(3) << newton(x0, f, grad) << "\n";
    }
}
