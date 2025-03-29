class GraphAdjacencyMatrix:
    def __init__(self, vertices: list[int], edges: list[list[int]]):
        # 顶点
        self.vertices: list[int] = []
        # 邻接矩阵
        self.adj_mat: list[list[int]] = []
        # 添加顶点
        for val in vertices:
            self.vertices.append(val)
        # 添加边
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def size(self) -> int:
        return len(self.vertices)

    def add_edge(self, v1, v2):
        return
