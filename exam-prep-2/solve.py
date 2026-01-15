from simple_queue import Queue
import minigraph as nx


# Dado un grafo dirigido SIN pesos y switches SW* ON/OFF 
# (que bloquean sus salidas), devuelve la lista de
# LEDs encendidos, es decir, aquellos LED* que están en 
# un camino activo Vcc -> ... -> LED -> ... -> GND
#
# Entrada:
#   V E
#   (E líneas) u v w
#   (opcionales) SWx=ON|OFF   # por defecto, todo SW* es ON
#
#   LEDs encendidos: [ ... ]

from simple_queue import Queue

# NOTAS:
# - main.py ya construye el grafo activo (MiniGraph) y compone la salida.
# - Aquí debes implementar SOLO la función pedida sobre el grafo activo.

def find_lit_leds(active_graph):
    """
    Ejercicio: LEDs encendidos por conectividad.

    Devuelve una lista (puede ser SIN ordenar) de los nodos LED* 
    donde existe un camino Vcc -> ... -> LED y LED -> ... -> GND 
    en el grafo activo.

    """
    
    # Forward traversal and backward traversal
    forward_reach = set()
    backward_reach = set()
    
    def dfs_f(node):
        if node in forward_reach:
            return
        forward_reach.add(node)
        for succ in active_graph.successors(node):
            dfs_f(succ)
    
    def dfs_b(node):
        if node in backward_reach:
            return
        backward_reach.add(node)
        for pre in active_graph.predecessors(node):
            dfs_b(pre)
    
    dfs_f("Vcc")
    dfs_b("GND")
    
    lit_leds = [led for led in forward_reach & backward_reach if "LED" in led]
    
    return lit_leds