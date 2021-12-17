import queue

import Queue
import Stack

visit = [0] * 9
stack2 = Stack.Stack(10)
etv = [0] * 10


def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i


class edgeNode:
    def __init__(self, adjvex=None, weight=None, next1=None, ):
        self.adjvex = adjvex
        self.weight = weight
        self.next1 = next1


class vertexNode:

    def __init__(self, data=None, in_count=None, first_edge=None):
        self.data = data
        self.in_count = in_count
        self.first_edge = first_edge


def topologicalsort(vertex, edge):
    stack = Stack.Stack(10)

    for i in range(len(vertex)):
        if vertex[i].in_count == 0:
            stack.push(vertex[i])
        i += 1
    count = 0
    while not stack.is_empty():
        top = stack.pop()
        stack2.push(top.data)
        count += 1
        print(top.data)
        aa = top.first_edge
        while aa is not None:
            vertex[aa.adjvex].in_count -= 1
            if vertex[aa.adjvex].in_count == 0:
                stack.push(vertex[aa.adjvex])

            if etv[int(top.data[1:])] + aa.weight > etv[aa.adjvex]:
                etv[aa.adjvex] = etv[int(top.data[1:])] + aa.weight

            aa = aa.next1

    if count < len(vertex):
        print('存在环')


def critical_path(vertex, edge):
    ete = []
    let = []
    ltv = [0] * 10
    topologicalsort(vertex, edge)
    for i in range(10):
        ltv[i] = etv[9]

    while not stack2.is_empty():
        gettop = stack2.pop()
        gettop = int(gettop[1:])
        bb = vertex[gettop].first_edge
        while bb is not None:
            k = bb.adjvex
            if ltv[k] - bb.weight < ltv[gettop]:
                ltv[gettop] = ltv[k] - bb.weight
            bb = bb.next1
    print(etv)
    print(ltv)

    for j in range(10):
        cc = vertex[j].first_edge
        while cc is not None:
            ete = etv[j]
            lte = ltv[cc.adjvex] - cc.weight
            if ete == lte:
                print(vertex[j].data, vertex[cc.adjvex].data)

            cc = cc.next1

        j += 1


class graph:
    def __init__(self):
        self.vertex = None
        self.edge = None

    def dfs(self, i):
        visit[i] = 1
        print(self.vertex[i])
        for j in range(9):
            if 0 < self.edge[i][j] < 99 and visit[j] != 1:
                self.dfs(j)
            j += 1

    def dfs_traverse(self):
        # size = len(self.vertex)
        for i in range(9):
            if visit[i] != 1:
                self.dfs(i)
            i += 1

    def bfs_traverse(self):
        queue1 = Queue.Queue()
        for i in range(9):
            visit[i] = 0
            i += 1
        for i in range(9):
            if visit[i] == 0:
                visit[i] = 1
                print(self.vertex[i])
                queue1.Enqueue(i)
            while not queue1.QueueEmpty():
                a = queue1.Dequeue()
                for j in range(9):
                    if 0 < self.edge[a][j] < 99 and visit[j] != 1:
                        visit[j] = 1
                        print(self.vertex[j])
                        queue1.Enqueue(j)
            j += 1

    def minispantree_prim(self):
        lostcost = [None] * 9
        adjvex = [None] * 9
        lostcost[0] = 0
        adjvex[0] = 0
        for i in range(9):
            lostcost[i] = self.edge[0][i]
            adjvex[i] = 0
            i += 1

        for v in range(1, 9):
            min = 99
            k = None
            for j in range(1, 9):
                if lostcost[j] != 0 and lostcost[j] < min:
                    min = lostcost[j]
                    k = j
                j += 1

            print('(' + str(adjvex[k]) + ',' + str(k) + ')')
            lostcost[k] = 0

            for m in range(1, 9):
                if self.edge[k][m] < lostcost[m] != 0:
                    lostcost[m] = self.edge[k][m]
                    adjvex[m] = k
                m += 1
            v += 1

    def minispantree_kruskal(self):
        edges = []
        for i in range(9):
            for j in range(i):
                if 0 < self.edge[i][j] < 99:
                    edges.append((i, j, self.edge[i][j]))

        for m in range(len(edges)):
            for n in range(m + 1, len(edges)):
                if edges[m][2] > edges[n][2]:
                    k = edges[m]
                    edges[m] = edges[n]
                    edges[n] = k
                n += 1
            m += 1

        parent = [None] * 9

        for l in range(9):
            parent[l] = l

        print(edges)

        for k in range(14):
            n = find(parent, edges[k][0])
            m = find(parent, edges[k][1])
            # print(n, m)
            if n != m:
                parent[n] = m
                print(edges[k])
            k += 1
            # print(parent)

    def shoresetpath_dijkstra(self):
        final = [0] * 9
        short_path = [0] * 9
        path = [0] * 9
        for i in range(9):
            short_path[i] = self.edge[0][i]
            i += 1

        final[0] = 1
        for j in range(9):
            min = 99
            for k in range(9):
                if short_path[k] < min and final[k] == 0:
                    min = short_path[k]
                    q = k
                k += 1
            final[q] = 1

            for l in range(9):
                if short_path[l] > min + self.edge[q][l] and final[l] != 1:
                    short_path[l] = min + self.edge[q][l]
                    path[l] = q
                l += 1

        print(short_path)
        print(path)

    def shoresetpath_floyd(self):
        short_path = self.edge.copy()
        print(short_path)
        path = [[0] * 9 for _ in range(9)]
        for m in range(9):
            for n in range(9):
                path[m][n] = n
                n += 1
            m += 1
        # print(path)
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    # print(i, j, k)
                    if short_path[j][k] > short_path[j][i] + short_path[i][k]:
                        short_path[j][k] = short_path[j][i] + short_path[i][k]
                        ww = path[j][i]
                        path[j][k] = ww
                    k += 1
                j += 1

            i += 1
        print(path)
        print(short_path)
        for x in range(9):
            for y in range(x + 1, 9):
                print(x, y, short_path[x][y])
                d = path[x][y]
                while d != y:
                    print(d)
                    d = path[d][y]

                print(y)
                y += 1
            print('----------------')
            x += 1
