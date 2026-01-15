include "globals.mzn";

% Número de donantes/receptores
int: n;
set of int: PARTICIPANTS = 1..n;

% Enumerado para las categorías (colores)
enum COLOR = {Azul, Naranja, Verde, Rojo};

% Matriz fija de compatibilidad (4x4) para los colores
array[COLOR, COLOR] of int: compatibility = [|
    100,  50,  20,   0 | % Azul
     50, 100,   0,  70 | % Naranja
     20,   0, 100,  60 | % Verde
      0,  70,  60, 100 | % Rojo
|];

% Categorías de los donantes y receptores
array[PARTICIPANTS] of COLOR: donor_categories;
array[PARTICIPANTS] of COLOR: recipient_categories;

% ------------------------------------ Resuelve el ejercicio a partir de aqui
array[PARTICIPANTS] of var PARTICIPANTS: matches;
var int: total;


% Constraints

constraint total = sum(i in PARTICIPANTS)(compatibility[donor_categories[i], recipient_categories[matches[i]]]); % Total is the sum of the entire compatibility

constraint alldifferent(matches);

solve maximize total;

output ["Compatibilidad total: \(show(total))\n", "Emparejamiento: \(show([matches[p] | p in PARTICIPANTS]))"];

