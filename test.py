import Sqlist
import Linklist
import Staticlist


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


staticlist_test()

