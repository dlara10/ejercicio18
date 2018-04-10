grafica2.pdf : EDO.py dat2.txt
	python EDO.py

grafica1.pdf : ejercicio18.py dat.txt
	python ejercicio18.py 

dat2.txt : e2
	./e2 > dat2.txt

dat.txt : ejercicio18
	./ejercicio18 > dat.txt

e2 :
	c++ ejer18.cpp -o e2

ejercicio18 : 
	c++ ejercicio18.cpp -o ejercicio18
