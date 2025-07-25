clc
format long
load puntos.txt -ascii

F = [1   28  -14.01; 
    1   250    -4.18;
    1   0   0;
    1   36  3.29];

x = puntos(:, 1);
z = puntos(:, 2);
y = puntos(:, 3);

F = [x.^0 x.^2.*z z.^1.5.*sin(x.^2)];


Y = [14
    8
    3
    20];

A = F'*F;
B = transpose(F)*Y;

c = A\B

%c = (F'*F)*(F'*Y);
