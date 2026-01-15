% Parámetros del problema
% Problema de flujo máximo en una red de tuberías de petróleo

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

% Rango de presión operativa seguro: [presión minima, presión máxima]
array[1..num_edges, 1..2] of int: pressure_range;

% Presión base de cada tubería (presión mínima sin flujo)
array[1..num_edges] of int: base_pressure;

% Constante conocida
int: k;

% Variable de decisión que representa el flujo máximo que llega al contenedor
var int: max_flow;

% Variable de decisión que indica el volumen de agua en cada tubería
array[1..num_edges] of var 0..max(capacity): flow;

% Poner el código a partir de aquí ------------------------------------------
constraint forall(e in 1..num_edges)(flow[e] >= 0 /\ flow[e] <= capacity[e]);

constraint forall(n in 1..num_nodes where n != source /\ n != sink)(sum(e in 1..num_edges where edges[e, 1] == n)(flow[e]) = sum(e in 1..num_edges where edges[e, 2] == n)(flow[e]));

constraint forall(e in 1..num_edges)(base_pressure[e] + k * flow[e] <= pressure_range[e, 2]);

constraint max_flow = sum(e in 1..num_edges where edges[e, 1] == source)(flow[e]);

% Objetivo
solve maximize max_flow;
