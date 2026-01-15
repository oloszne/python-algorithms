# --------------------------------------------------------------------- Graph

class Graph():
    def __init__(self):
        self.graph = MiniGraph()

    def add_node(self, nodeid):
        self.graph.add_node (nodeid)

    def add_edge(self, u, v, weight=None):
        if not weight:
           self.graph.add_edge (u, v, data={}, directed=False)
        else:
           self.graph.add_edge (u, v, data={'weight':weight}, directed=False)

    def number_of_nodes(self):
        return len(self.graph.nodes())

    def number_of_edges(self):
        return len(self.graph.edges())

    def nodes(self):
        return [id for id,_ in self.graph.nodes()]

    def edges(self, u=None, data=False):
        if (not u) and (not data):
           return [(u,v) for u,v,_,_,_ in self.graph.edges()]
        elif not u and data:
           return [(u,v,d) for u,v,_,d,_ in self.graph.edges()]
        elif u and not data:
           return [(u1,v1) for u1,v1,_,d,_ in self.graph.edges() if u1==u] + \
                  [(v1,u1) for u1,v1,_,d,_ in self.graph.edges() if v1==u]
        else:
           return [(u1,v1,d) for u1,v1,_,d,_ in self.graph.edges() if u1==u] + \
                  [(v1,u1,d) for u1,v1,_,d,_ in self.graph.edges() if v1==u]

    def neighbors(self, u):
        return list(set([v1 for u1,v1,_,_,_ in self.graph.edges() if u1==u] + \
                        [u1 for u1,v1,_,_,_ in self.graph.edges() if v1==u]))

    def degree(self, u):
        return self.graph.degree(u)

# --------------------------------------------------------------------- DiGraph

class DiGraph():
    def __init__(self):
        self.graph = MiniGraph()

    def add_node(self, nodeid):
        self.graph.add_node (nodeid)

    def add_edge(self, u, v, weight=None):
        if not weight:
           self.graph.add_edge (u, v, directed=True)
        else:
           self.graph.add_edge (u, v, data={'weight':weight}, directed=True)

    def number_of_nodes(self):
        return len(self.graph.nodes())

    def number_of_edges(self):
        return len(self.graph.edges())

    def nodes(self):
        return [id for id,_ in self.graph.nodes()]

    def edges(self, u=None, data=False):
        if (not u) and (not data):
           return [(u,v) for u,v,_,_,_ in self.graph.edges()]
        elif not u and data:
           return [(u,v,d) for u,v,_,d,_ in self.graph.edges()]
        elif u and not data:
           return [(u1,v1) for u1,v1,_,d,_ in self.graph.edges() if u1==u]
        else:
           return [(u1,v1,d) for u1,v1,_,d,_ in self.graph.edges() if u1==u]

    def in_edges(self, u, data=False):
        if not data:
           return [(u1,v1) for u1,v1,_,d,_ in self.graph.edges() if v1==u]
        else:
           return [(u1,v1,d) for u1,v1,_,d,_ in self.graph.edges() if v1==u]

    def out_edges(self, u, data=False):
        if not data:
           return [(u1,v1) for u1,v1,_,d,_ in self.graph.edges() if u1==u]
        else:
           return [(u1,v1,d) for u1,v1,_,d,_ in self.graph.edges() if u1==u]

    def neighbors(self, u):
        return self.successors(u)

    def successors(self, u):
        return list(set([v1 for u1,v1,_,_,_ in self.graph.edges() if u1==u]))

    def predecessors(self, v):
        return list(set([u1 for u1,v1,_,_,_ in self.graph.edges() if v1==v]))

    def in_degree(self, u):
        return self.graph.in_degree(u)

    def out_degree(self, u):
        return self.graph.out_degree(u)

# ----------------------------------------------------------------- MiniGraph
import warnings
from collections import namedtuple, defaultdict

class MiniGraphError(Exception): pass
class MiniGraphWarning(Warning): pass

class MiniGraph(object):

    __slots__ = ('_graph',)

    def __init__(self, nodes=None, edges=None):
        self._graph = {}
        if nodes is None: nodes = {}
        self.add_nodes(nodes)
        if edges is None: edges = {}
        self.add_edges(edges)

    def add_node(self, nodeid, data=None):
        if data is None:
            data = {}
        if nodeid in self._graph:
            self._graph[nodeid][1].update(data)
        else:
            self._graph[nodeid] = (nodeid, data, {}, {})

    def add_nodes(self, nodes):
        for node in nodes:
            try:
                node, data = node
            except TypeError:
                data = {}
            self.add_node(node, data=data)

    def remove_node(self, nodeid):
        g = self._graph
        if nodeid not in g:
            raise KeyError(nodeid)
        _prune_edges(g, nodeid)
        del g[nodeid]

    def node(self, nodeid):
        return self._graph[nodeid]

    def nodes(self):
        return [(nid, n[1]) for nid, n in self._graph.items()]

    def add_edge(self, start, end, label=None, data=None, directed=True):
        self.add_edges([(start, end, label, data, directed)])

    #@profile
    def add_edges(self, edges):
        g = self._graph
        add_edge = _add_edge

        for edge in edges:
            edgelen = len(edge)
            if edgelen == 5:
                start, end, label, data, directed = edge
            elif edgelen == 2:
                start, end = edge; label = data = None; directed = True
            elif edgelen == 4:
                start, end, label, data = edge; directed = True
            elif edgelen == 3:
                start, end, label = edge; data = None; directed = True
            else:
                raise MiniGraphError('Invalid edge: {}'.format(edge))

            if data is None: data = {}
            if start not in g: g[start] = (start, {}, {}, {})
            if end not in g: g[end] = (end, {}, {}, {})

            e = (start, end, label, data, directed)

            #add_edge(g[start][2], label, end, e)
            d = g[start][2]
            if label not in d:
                d[label] = innerdict = {}
            else:
                innerdict = d[label]
            if end not in innerdict:
                innerdict[end] = e
            else:
                if innerdict[end][4] != e[4]:
                    raise MiniGraphError(
                        'Cannot update directed and undirected edges.'
                    )
                innerdict[end][3].update(e[3])
            
            #add_edge(g[end][3], label, start, e)
            d = g[end][3]
            if label not in d:
                d[label] = innerdict = {}
            else:
                innerdict = d[label]
            if start not in innerdict:
                innerdict[start] = e
            else:
                if innerdict[start][4] != e[4]:
                    raise MiniGraphError(
                        'Cannot update directed and undirected edges.'
                    )
                innerdict[start][3].update(e[3])

            if directed is False:
                #add_edge(g[end][2], label, start, e)
                d = g[end][2]
                if label not in d:
                    d[label] = innerdict = {}
                else:
                    innerdict = d[label]
                if start not in innerdict:
                    innerdict[start] = e
                else:
                    if innerdict[start][4] != e[4]:
                        raise MiniGraphError(
                            'Cannot update directed and undirected edges.'
                        )
                    innerdict[start][3].update(e[3])

                #add_edge(g[start][3], label, end, e)
                d = g[start][3]
                if label not in d:
                    d[label] = innerdict = {}
                else:
                    innerdict = d[label]
                if end not in innerdict:
                    innerdict[end] = e
                else:
                    if innerdict[end][4] != e[4]:
                        raise MiniGraphError(
                            'Cannot update directed and undirected edges.'
                        )
                    innerdict[end][3].update(e[3])

    def remove_edge(self, start, end, label=None, directed=None):
        g = self._graph
        if start not in g: raise KeyError(start)
        edges = g[start][2]
        if label not in edges: raise KeyError(label)
        if end not in edges[label]: raise KeyError(end)
        _dir = g[start][2][label][end][4]
        if directed is not None:
            assert _dir == directed

        try:
            in_edges = g[end][3]
            del edges[label][end]
            if len(edges[label]) == 0:
                del edges[label]
            del in_edges[label][start]
            if len(in_edges[label]) == 0:
                del in_edges[label]
            # undirected links are listed twice (except simple loops)
            if not _dir and start != end:
                edges = g[end][2]
                in_edges = g[start][3]
                del edges[label][start]
                if len(edges[label]) == 0:
                    del edges[label]
                del in_edges[label][end]
                if len(in_edges[label]) == 0:
                    del in_edges[label]

        except KeyError:
            raise
            warnings.warn(
                'Unexpected KeyError while removing {} edge ({}, {}, {})'
                .format('directed' if directed else 'undirected',
                        start, end, label),
                MiniGraphWarning
            )

    def edge(self, start, end, label=None, directed=None):
        e = self._graph[start][2][label][end]
        if directed is not None:
            assert e[4] == directed
        return e

    def edges(self):
        return [e
            for nid, n in self._graph.items()
            for ed in n[2].values()
            for e in ed.values()
            # only include undirected links from the source node (whatever
            # the source node was when it was instantiated)
            if e[4] or e[0] == nid
        ]

    def order(self):
        return len(self._graph)

    def size(self):
        return len(self.edges())

    def degree(self, nodeid):
        n = self._graph[nodeid]
        return (
            sum(len(ed) for ed in n[2].values()) +
            len([
                e for ed in n[3].values() for e in ed.values()
                # only count undirected edges here if they are simple loops
                if e[4] or e[0] == e[1]
            ])
        )

    def out_degree(self, nodeid):
        n = self._graph[nodeid]
        return sum(len(ed) for ed in n[2].values())
        # return (
        #     sum(len(ed) for ed in n[2].values()) +
        #     len([e  for ed in n[3].values()
        #             for e in ed.values()
        #             if e[4] == False and e[0] != e[1]])
        # )

    def in_degree(self, nodeid):
        n = self._graph[nodeid]
        return sum(len(ed) for ed in n[3].values())
        # return (
        #     sum(len(ed) for ed in n[3].values()) +
        #     len([e  for ed in n[2].values()
        #             for e in ed.values()
        #             if e[4] == False and e[0] != e[1]])
        # )

    def subgraph(self, nodeids):
        g = self._graph
        nidset = set(nodeids)
        return MiniGraph(
            nodes=[(nid, g[nid][1]) for nid in nodeids],
            edges=[e for start in nodeids
                     for label, ed in g[start][2].items()
                     for end, e in ed.items() if end in nidset]
        )

# for a bit more speed, this can be inlined directly
def _add_edge(d, label, idx, e):
    if label not in d:
        d[label] = innerdict = {}
    else:
        innerdict = d[label]
    if idx not in innerdict:
        innerdict[idx] = e
    else:
        if innerdict[idx][4] != e[4]:
            raise MiniGraphError(
                'Cannot update directed and undirected edges.'
            )
        innerdict[idx][3].update(e[3])
