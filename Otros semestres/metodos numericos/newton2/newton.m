clc
format long

syms x;

f = input("teclee la funcion ")

fprima = diff(f,x,1)

x =(1+1i)

while eval(abs(f))>1E-8
    
    x = x - eval(f)/eval(fprima)

end