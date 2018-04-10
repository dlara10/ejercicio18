#include <iostream>

using std::cout;
using std::endl;

int main(){

float x;
float h;
float N;
float z = 0.0;
float y = 1.0;
int i;

x = 0.0, h = 0.1, N = 10/h;

for(i = 0; i < N; i ++){
	z = z - h*y;
	y = y + h*z;
	x = x + h;
	cout << x << " " << y << " " << z << endl;
	}

return 0;
}
