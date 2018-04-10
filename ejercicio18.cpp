# include <iostream>

using std::cout;
using std::endl;

int main(){

float x = 0.0;
float h = 0.1;
float N = 3/h;
float y;

for (int i = 0; i < N; i ++){
	x = x + h;
	y = y - h*y;
cout << x << " " << y<< endl;	
}
return 0;

}
