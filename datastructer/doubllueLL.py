# #이중 링크드 리스트
# class DLinkedList:

#     #D_L_list에서 쓸 노드
#     class Node:
#         def __init__(self, v, n = None, p = None):
#             self.value = v #저장된 데이터
#             self.next = n #다음 노드 가리키는 변수
#             self.prev = p #이전 노드 가리키는 변수

#     #D_L_List에서 필요한 변수
#     def __init__(self):
#         self.head = None #첫 생성시 내부에는 노드가 없으므로
#         self.tail = None

# ##테스트
# if __name__=="__main__":
#     dl = DLinkedList()

#이중 링크드 리스트
class DLinkedList:

    #create
   class Node :
       def __init__(self,v,n = None ,p = None) :
            self.head = None
            self.next = n
            self.tail = p
    #init
    def __init__(self) :
        self.head = None #첫 생성시 내부에는 노드가 없으므로
        self.tail = None
    
    #insert
    def insertNodeBefore(self,v) :
        if self.head is None :
            self.head = self.Node(v)
            self.tail = self.head
        else :
            self.head.prev = self.Node(v,n=self.head)
            self.head = self.head.prev

    def insertNodeBefore(self,v) :
        if self.tail is None :
            self.tail = self.Node(v)
            self.head = self.tail
        else : 
            self.tail.next = self.Node(v,p=self.tail)
            self.tail = self.tail.next

    #print
    def printNodeBefore(self) :
        if self.head is None :
            return 'theres no data in list'
        
        else :
            link = self.head
            while link :
                print(link.value)
                link = link.next
            print()
        return
    
    def printNodeAfter(self) :
        if self.tail is None :
            return 'theres no data in list'
        else :
            link = self.tail
            while link :
                print(link.value)
                link = link.prev
            print()
    
    #delete
    def deleteNodeBefore(self) :
        if self.head is None :
            print('theres no data in list')
            return
        else :
            self.head = self.head.next
            self.head.prev = None
    
    def deleteNodeAfter(self) :
        if self.tail in None :
            print('theres no data in list')
            return
        else :
            self.tail = self.tail.prev
            self.tail.next = None

    #serach
    def serachNodeBefore(self,v) :
        if self.head is None :
            print('theres no data in list')
            return
        else :
            link = self.head
            index = 0
            while link :
                if link.value == v :
                    print(index)
                else :
                    link = link.next
                    index += 1
            
    def searchNodeAfter(self,v) :
        if self.tail is None :
            print('theres no data')
            return
        else :
            link = self.tail
            index = 0
            while link :
                if link.value == v :
                    print(index)
                else :
                    link = link.prev
                    index -= 1
                    
##테스트
if __name__=="__main__":
    dl = DLinkedList()
    dl.insertNodeAfter('FirstData') #head삽입 테스트
    dl.insertNodeBefore('LastData') #tail삽입 테스트