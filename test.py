import Sqlist
import Linklist


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
    print(list1.getElem(2))


linklist_test()
