% Problema del Flujo de Agua en un Sistema de Tuberías con Estaciones de Bombeo

% Número de puntos de conexión en el sistema
int: num_nodes;

% Número de tuberías en el sistema
int: num_edges;

% Fuente principal
int: source;

% Contenedor o depósito final
int: sink;

% Definición de las tuberías: [punto de entrada, punto de salida]
array[1..num_edges, 1..2] of int: edges;

% Capacidad de cada tubería en litros/segundo
array[1..num_edges] of int: capacity;

% Capacidad de manejo de las estaciones de bombeo. Usamos -1 para los puntos que no son estaciones.
array[1..num_nodes] of int: node_capacity;

% Salida
output
[
"max flow =" ++ show(max_flow)
];

% Variable de decisión que representa el flujo máximo que llega al contenedor
var int: max_flow;

% Variable de decisión que indica el volumen de agua en cada tubería
array[1..num_edges] of var int: flow;

% ------------------------------------ Resuelve el ejercicio a partir de aqui
constraint forall(e in 1..num_edges)(flow[e] >= 0 /\ flow[e] <= capacity[e]); % Flow rate always has to be a positive number and not exceed cap.

constraint forall(n in 1..num_nodes where node_capacity[n] != -1)(sum(e in 1..num_edges where edges[e, 2] == n)(flow[e]) <= node_capacity[n]); % Node cap constraint

constraint forall(n in 1..num_nodes where n != source /\ n != sink)(sum(e in 1..num_edges where edges[e, 1] == n)(flow[e]) = sum(e in 1..num_edges where edges[e, 2] == n)(flow[e])); % In-Out Equillibrium

constraint max_flow = sum(e in 1..num_edges where edges[e, 1] = source)(flow[e]); % Max flow calculation

solve maximize max_flow;



