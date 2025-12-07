int: n;
array[1..n] of int: value;

%Introduzca el código a partir de esta línea
array[1..n] of var 0..1: taken;
var int: total_value;

%Multiply house values with binary taken elements (rob or not rob)
constraint total_value = sum(i in 1..n) (taken[i] * value[i]);

%Logic constraint - can't steal from adjacent houses
constraint forall(i in 1..n-1) (taken[i] + taken[i+1] <= 1);

%Maximize result (value of house robbed)
solve maximize total_value;

%Output
output [
    "taken = \(taken);\n",
    "Total Value = \(total_value);"
];