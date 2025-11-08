var 1..10: x;
constraint x mod 4 = 0;

var int: obj = (x - 7) * (x - 7);
solve minimize obj;

output["x= ", show(x), "\n",
       "obj=", show(obj)];