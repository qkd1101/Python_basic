# class SLinkedList:
#     class Node:
#         def __init__(self,v,n = None):
#             self.value = v #값
#             self.next = n  #다음 노드
    
#     def __init__(self) :
#         self.head = None

# if __name__=="__main__":
#     sl = SLinkedList()

#put,print list data
# class SLinkedList:

#     #S_L_list에서 쓸 노드
#     class Node:
#         def __init__(self, v, n = None):
#             self.value = v #저장된 데이터
#             self.next = n #다음 노드 가리키는 변수

#     #S_L_List에서 필요한 변수
#     def __init__(self):
#         self.head = None #첫 생성시 내부에는 노드가 없으므로
    
#     #insert
#     def insertNode(self,v) :
#         if self.head is None :
#             self.head = self.Node(v)
        
#         else : self.head = self.Node(v,self.head)

#     #print
#     def printNode(self) :
#         if self.head is None :
#             print("no data")
#             return
#         else : 
#             print("리스트 구조 : ")
#             link = self.head

#             while link :
#                 print(link.value,'->',end=' ')
#                 link = link.next
#             print()

#     #delete
#     def deleteNode(self) :
#         if self.head is None :
#             print("no data")
#             return
#         else :
#             self.head = self.head.next

#     #search
#     def searchNode(self,serachValue) :
#         if self.head is None :
#             print("no data")
#             return
#         else :
#             link = self.head
#             index = 0
#             while link :
#                 if link.value == serachValue :
#                     return index
#                 else : 
#                     link = link.next
#                     index += 1
#             return 'theres no data in List'


# if __name__=="__main__":
#     sl = SLinkedList()
#     sl.insertNode('1st')
#     sl.insertNode('2nd')
#     sl.insertNode('3rd')
#     sl.printNode()
#     sl.deleteNode()
#     sl.deleteNode()
#     sl.deleteNode()
#     sl.printNode()
#     sl.insertNode('2nd')
#     sl.insertNode('3rd')
#     print(sl.searchNode('2nd'))
#     sl.deleteNode()
#     sl.printNode()
#     print(sl.searchNode('3rd'))
#     sl.deleteNode()
#     sl.deleteNode()
#     sl.printNode()

class singleLinkedList() :
    #create
    class Node :
        def __init__(self,v,n = None) :
            self.value = v
            self.next = n

    def __init__(self) :
        self.head = None
    
    #insert
    def insertNode(self,v) :
        if self.head is None :
            self.head = self.Node(v)
        
        else : self.head = self.Node(v,self.head)
    #delete
    def deleteNode(self) :
        if self.head is None :
            print("no data to delete")
            return 
        else :
            self.head = self.head.next
    #print
    def printNode(self) :
        if self.head is None :
            print("no data to print")
            return
        else :
            link = self.head
            while link :
                print(link.value,'->',end=' ')
                link = link.next
            print()
    #search
    def searchNode(self,v) :
        if self.head is None :
            return "no data to search"
        else :
            link = self.head
            i = 0
            while link :
                if link.value == v :
                    return i
                else :
                    i += 1
                    link = link.next
            return "no data at list"        

if __name__=="__main__":
    sl = singleLinkedList()
    sl.insertNode('1')
    sl.insertNode('2')
    sl.insertNode('3')
    sl.printNode()

    sl.deleteNode()
    sl.deleteNode()
    sl.insertNode('3')
    sl.insertNode('2')
    sl.printNode()

    print(sl.searchNode('1'))
    print(sl.searchNode('8'))