# solve.py — ESQUELETO (alumno)
#
# Dado un grafo dirigido con posibles interruptores SW* (ON/OFF), 
# considera activas solo las aristas cuyo origen está ON. 
# Comprueba si TODOS los nodos están en algún camino activo 
# desde Vcc hasta GND. 
#
# Retorna:
#  1) Componentes en camino Vcc -> ... -> GND (intersección): [lista_ordenada]
#  2) Componentes desconectados: [lista_ordenada]
#
# Formato de entrada:
#  - L1: V E
#  - L2.. L(E+1): u v (aristas dirigidas)
#  - Resto (opcional): líneas "SWx=ON|OFF"
#
# Reglas:
#  - Un interruptor no declarado se considera ON.
#  - Solo se desactivan aristas si "su origen" es SWx=OFF.
#  - "Conectado" significa: todo nodo pertenece a algún camino Vcc -> ... -> GND.

from typing import List, Set
import minigraph as nx
from simple_queue import Queue


def check_circuit_connectivity(G: nx.DiGraph):
    # Evalúa la conectividad completa del circuito representado por el grafo
    # y devuelve (on_path_list, disconnected_list), donde on_path_list
    # son los nodos que están en algún camino Vcc -> ... -> GND
    # (excluyendo en ambas listas `Vcc`, `GND` y nodos `SW*`)
    
    # Por ahora, devolver listas vacías como esqueleto
    # Forward traversal and backward traversal
    forward_reach = set()
    backward_reach = set()
    
    def dfs_f(node):
        if node in forward_reach:
            return
        forward_reach.add(node)
        for succ in G.successors(node):
            dfs_f(succ)
    
    def dfs_b(node):
        if node in backward_reach:
            return
        backward_reach.add(node)
        for pre in G.predecessors(node):
            dfs_b(pre)
    
    dfs_f("Vcc")
    dfs_b("GND")
    
    connected = [c for c in forward_reach & backward_reach if not "Vcc" or "GND" or "SW" in c]
    disconnected = [d for d in forward_reach ^ backward_reach if not "Vcc" or "GND" or "SW" in d]
     
    return connected, disconnected