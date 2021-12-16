from GraphAlgoInterface import GraphAlgoInterface



class GraphAlgo(GraphAlgoInterface):
    def __init__(self, dg: DiGraph = None):
        self.graph = DiGraph