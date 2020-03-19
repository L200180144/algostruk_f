##-----------------------------NO. 5-----------------------------
class node (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next
    def cari (self, cari):
        curNode = self
        while curNode is not None :
            if curNode.next != None :
                if curNode.data != cari :
                    curNode = curNode.next
                else :
                    print ("Item", cari, "ada dalam Linked List")
                    break
            elif curNode.next == None :
                print ("Item", cari, "tidak ada linked list")
                break
a = node (12)
menu = a
a.next = node (34)
a = a.next
a.next = node (10)
a = a.next
a.next = node (45)

print ("\n-----------------------------NO. 5-----------------------------")
menu.cari(10)
menu.cari(110)
