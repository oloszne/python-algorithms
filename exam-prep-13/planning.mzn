include "globals.mzn";

int: n;  % Número de envíos
int: k;  % Número de transportistas disponibles
int: t;  % Número de camiones disponibles

array[1..n] of int: durations;      % Duración de cada envío
array[1..n] of int: transportistas; % Transportistas necesarios para cada envío
array[1..n] of int: camiones;       % Camiones necesarios para cada envío
array[1..n] of int: priorities;     % Prioridad de cada envío

% Decision variables
array[1..n] of var 0..sum(durations): start_times;
var 0..sum(durations): total_time;

% Constraints

% Each volunteer and each vehicle can only participate in one shipment at a time. CUMULATIVE
constraint cumulative(start_times, durations, transportistas, k);
constraint cumulative(start_times, durations, camiones, t);

% Shipments can't start at the same time
constraint alldifferent(start_times);

% Shipments with priority 1 have to start before shipments with priority 2
constraint forall(i, j in 1..n where priorities[i] < priorities[j]) (
    start_times[i] <= start_times[j]
);

constraint forall(i in 1..n) (
    total_time >= start_times[i] + durations[i]
);

solve minimize total_time;

output [
    "Tiempo total: \(show(total_time))\n",
    "\(show([start_times[i] | i in 1..n]))"
];

% ----------------------- Resuelve el ejercicio a partir de aqui
