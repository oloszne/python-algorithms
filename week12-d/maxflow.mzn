int: num_nodes;                          % número de nodos del grafo
int: num_edges;                          % número de aristas del grafo

1..num_nodes:source;                     % nodo fuente
1..num_nodes:sink;                       % nodo sumidero

array[1..num_edges, 1..2] of int: edges; % aristas del grafo (origen->destino)
array[1..num_edges] of int: capacity;    % capacidad de cada arista

var int: max_flow;                       % variable de decision para el valor
                                         % del flujo máximo
array[1..num_edges] of var int: flow;    % variable de decisión para el flujo
                                         % final de cada arista

output
[ 
  "max flow =" ++ show(max_flow)
];

% Escribir el código a partir de aquí-----------------------------------------

% 1. Capacity Constraint
constraint forall(i in 1..num_edges) (flow[i] >= 0 /\ flow[i] <= capacity[i]);
% 2. Inflow, Outflow Equilibrium Constraint
constraint forall(n in 1..num_nodes) (
    let {
        % Outflow
        var int: flow_out = sum(e in 1..num_edges where edges[e,1] == n) (flow[e]);
        % Inflow
        var int: flow_in  = sum(e in 1..num_edges where edges[e,2] == n) (flow[e]);
    } in
    
    if n == source then
        flow_out - flow_in == max_flow
    elseif n == sink then
        flow_in - flow_out == max_flow
    else
        flow_out == flow_in
    endif
 );

solve maximize max_flow;