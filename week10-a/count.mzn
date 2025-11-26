var 100..500: x;

constraint x mod 5 == 2;
constraint x mod 7 == 2;
constraint x mod 12 == 1;

solve satisfy;
output["army = ", show(x)];
