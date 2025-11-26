include "globals.mzn";

enum Women = {Ana, Marta, Patricia};
enum Men = {Carlos, Marco, Juan};

array[Women, Men] of int: wrank = [|1, 2, 3, |3, 2, 1, |3, 1, 2|];
array[Men, Women] of int: mrank = [|2, 1, 3, |1, 2, 3, |1, 3, 2|];

%Escribir el código a partir de aquí
array[Men] of var Women: wife;
array[Women] of var Men: husband;

constraint forall(m in Men) (husband[wife[m]] == m);
constraint forall(w in Women) (wife[husband[w]] == w);

constraint forall(m in Men, o in Women) (
    if mrank[m, o] < mrank[m, wife[m]] then
        wrank[o, husband[o]] < wrank[o, m]
    else 
        true
    endif
);

var int: obj_men = sum(m in Men)(bool2int(mrank[m, wife[m]] == 1));
var int: obj_women = sum(w in Women)(bool2int(wrank[w, husband[w]] == 1));

solve minimize abs(obj_men - obj_women);

output [
  "wife: \(wife)\n",
  "husband: \(husband)\n",
  "obj_men:\(obj_men)\n",
  "obj_women:\(obj_women)\n"
];