int: n; 
int: capacity; 
set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;

%Escribir el código a partir de aquí
array[1..n] of var 0..2: taken;
var int: total_value;

%Calculate value
constraint total_value = sum(i in 1..n) (taken[i] * value[i]);

%Capacity constraint
constraint sum(i in 1..n)(weight[i] * taken[i]) <= capacity;
%

solve maximize total_value;

output [
    "taken = \(taken);\n",
    "Total Value = \(total_value);"
];
