import Sqlist
import Linklist
import Staticlist
import Stack
import SqQueue
import tree
import graph
import sort


def sqlist_test():
    list1 = Sqlist.Sqlist(5)
    for j in range(5):
        list1.listAppend(j)
    print(list1.getElem(3))
    print(list1.locateElem(4))
    print(list1.locateElem(6))
    print(list1.is_full())
    print(list1.is_empty())
    print(list1.length())
    list1.listDelete(3)
    list1.listDelete(3)
    list1.listInsert(4, 9)
    # list1.listDelete(4)
    list1.listPrint()
    # list1.listDelete(4)
    # list1.listInsert(2, 9)
    # list1.listPrint()
    # list1.listInsert(3, 9)
    # list1.listInsert(3, 5)
    # list1.clearlist()
    # print(list1.data)


def linklist_test():
    list1 = Linklist.Linklist()
    for j in range(6):
        # list1.listAppend(j)
        list1.listAdd(j)
    list1.listInsert(7, 7)
    list1.listPrint()
    print(list1.len)
    list1.listDelete(4)
    list1.listPrint()
    print(list1.len)
    print(list1.locateElem(9))
    print(list1.getElem(3))


def staticlist_test():
    list1 = Staticlist.Staticlist(6)

    for j in range(6):
        # list1.list_append(j)
        list1.list_add(j)
    # list1.list_print()
    list1.list_delete(3)
    list1.list_delete(3)
    list1.list_print()
    # print(list1.get_elem(3))
    print(list1.locate_elem(3))
    # list1.list_insert(3, 9)
    # print(list1.len)


def stack_test():
    stack = Stack.Stack(6)
    for j in range(6):
        stack.push(j)
    stack.stack_print()
    stack.pop()
    stack.push(6)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.stack_print()
    # print(stack.get_top())
    print(stack.stack_length())


def sqqueue_test():
    sqqueue = SqQueue.SqQueue(6)
    print(sqqueue.item)
    for j in range(5):
        sqqueue.Enqueue(j)
    sqqueue.QueuePrint()
    sqqueue.Dequeue()
    sqqueue.Dequeue()
    sqqueue.Dequeue()
    sqqueue.Dequeue()
    print('---------------')
    print(sqqueue.item)
    sqqueue.QueuePrint()
    sqqueue.Enqueue(7)
    sqqueue.Enqueue(8)
    sqqueue.Enqueue(9)
    print('---------------')
    print(sqqueue.item)
    print(sqqueue.front)
    print(sqqueue.rear)
    print(sqqueue.len)
    sqqueue.QueuePrint()


# ABDH##I##E##CF#J##G##A
def tree_test():
    tree1 = tree.Tree()
    tree.create_bitree(tree1, True)
    tree.inordertraverse(tree1.root)
    tree.intreading(tree1.root)
    tree.inordertraverse_thr(tree1.root)
    # print('-------------------')
    # tree.inordertraverse(tree1.root)
    # print('-------------------')
    # tree.postordertraverse(tree1.root)


def graph_test():
    graph1 = graph.graph()
    graph1.vertex = ['v0', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8']
    graph1.edge = [[0, 10, 99, 99, 99, 11, 99, 99, 99],
                   [10, 0, 18, 99, 99, 99, 16, 99, 12],
                   [99, 18, 0, 22, 99, 99, 99, 99, 8],
                   [99, 99, 22, 0, 20, 99, 99, 16, 21],
                   [99, 99, 99, 20, 0, 26, 99, 7, 99],
                   [11, 99, 99, 99, 26, 0, 17, 99, 99],
                   [99, 16, 99, 99, 99, 17, 0, 19, 99],
                   [99, 99, 99, 16, 7, 99, 19, 0, 99],
                   [99, 12, 8, 21, 99, 99, 99, 99, 0]]

    # graph1.dfs_traverse()
    # graph1.bfs_traverse()
    # graph1.minispantree_prim()
    # graph1.minispantree_kruskal()
    # graph1.minispantree_kruskal()
    # graph1.shoresetpath_dijkstra()
    # [0, 10, 28, 43, 37, 11, 26, 44, 22]
    # [0, 0, 1, 8, 5, 0, 1, 4, 1]
    # graph1.shoresetpath_floyd()

    vertex0 = graph.vertexNode('v0', 0)
    vertex1 = graph.vertexNode('v1', 1)
    vertex2 = graph.vertexNode('v2', 1)
    vertex3 = graph.vertexNode('v3', 2)
    vertex4 = graph.vertexNode('v4', 2)
    vertex5 = graph.vertexNode('v5', 1)
    vertex6 = graph.vertexNode('v6', 1)
    vertex7 = graph.vertexNode('v7', 2)
    vertex8 = graph.vertexNode('v8', 1)
    vertex9 = graph.vertexNode('v9', 2)
    edge1 = graph.edgeNode(2, 4)
    edge2 = graph.edgeNode(4, 6)
    edge3 = graph.edgeNode(5, 7)
    edge4 = graph.edgeNode(4, 3)
    edge5 = graph.edgeNode(7, 4)
    edge6 = graph.edgeNode(7, 6)
    edge7 = graph.edgeNode(9, 2)
    edge8 = graph.edgeNode(8, 5)
    edge9 = graph.edgeNode(9, 3)
    edge10 = graph.edgeNode(1, 3)
    edge11 = graph.edgeNode(3, 5)
    edge12 = graph.edgeNode(3, 8)
    edge13 = graph.edgeNode(6, 9)

    vertex0.first_edge = edge1
    edge1.next1 = edge10
    vertex1.first_edge = edge2
    edge2.next1 = edge11
    vertex2.first_edge = edge3
    edge3.next1 = edge12
    vertex3.first_edge = edge4
    vertex4.first_edge = edge5
    edge5.next1 = edge13
    vertex5.first_edge = edge6
    vertex6.first_edge = edge7
    vertex7.first_edge = edge8
    vertex8.first_edge = edge9

    vertexs = [vertex0, vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7, vertex8, vertex9]
    edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, edge13]
    # graph.topologicalsort(vertexs, edges)
    graph.critical_path(vertexs, edges)


def sort_test():
    # data = [9, 1, 5, 8, 3, 7, 4, 6, 2]
    # sort.bubble_sort(data)
    # sort.select_sort(data)
    # sort.insert_sort(data)
    data = [50, 10, 90, 30, 70, 40, 80, 60, 20]
    # sort.shell_sort(data)
    # sort.heap_sort(data)
    # sort.merge_sort(data)
    # sort.merge_sort2(data)
    sort.quick_sort(data)
    print(data)
    # print(data)


sort_test()