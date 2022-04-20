
class Node:
    def __init__(self,item=None,link=None):
        self.item,self.link = item,link
class LinkedList:
    def __init__(self):
        self.head = None                    #인스턴스의 헤드 
        
    def print_list(self):
        node = self.head # 헤드노드
        print('h->', end ="")
        while node is not None: #while node != None: 
            print ("{}->".format(node.item), end="")
            node = node.link
        print(None)
        
    def insert_node(self, p, new_node):     # p = prev
        if self.head is None:               # 빈 리스트라면 (노드가없음)
            self.head = new_node            # 헤드는 새로운 노드를 가리킨다.
        elif p is None:                     # 링크가 리스트의첫번째(헤드)를 가리키고있을때 
            new_node.link = self.head       # 추가할 노드가 (과거)헤드를 가리킴
            self.head = new_node            # 뉴노드가 헤드가됨
        else :                              # 일반적인 상황
            new_node.link = p.link          # a1 과 a2 사이에 삽입한다 할 때  p = a1 // 이전노드의 링크(a2를 가리킴) , newnode의 link = a2
            p.link = new_node               # p는 이제 new_node를 가리킴 
            
    def delete_node(self, p, removed):      # removed 는 삭제할 노드 , p 는 삭제할 노드의 전 노드
        if removed == self.head:            # 삭제할 노드가 헤드노드일 때
            self.head = removed.link        # 삭제할 노드의 링크하는 노드를 헤드로 초기화
        else :                              # 일반적인 상황
            p.link = removed.link           # 삭제할 노드의 전 노드의 링크를 삭제할 노드의 링크로 초기화
        del removed
        
    def insert_first(self, item):           # item = elem = key값
        new_node = Node(item)               # new_node 라는 인스턴스 생성
        self.insert_node(p=None, new_node=new_node)
        
    def insert_last(self, item):
        new_node = Node(item)
        p = self.head                       #p 를 head 를 설정하고 와일문으로 tail 찾기
        while(p != None)and(p.link != None):#p.link가 none 이라면 p 가 tail 임
            p = p.link
        self.insert_node(p=p, new_node =new_node)
    
    def search(self, item):                 # item 찾아서 노드 리턴
        node = self.head
        while node is not None:             
            if node.item==item:             # 찾았다면
                return node                 # 해당노드 반환
        node = node.link                    # 노드를 노드가 가리키는 노드로 초기화
        return node
        
    def search_prev(self, item):
        p = None
        node = self.head
        while node is not None:
            if node.item == item:
                return node, p
            p = node
            node = node.link
        return None, p                      # while 내에서 반환하던 오류 수정
    def delete(self, item):
        removed, p = self.search_prev(item)
        if removed is None:                 #삭제할 아이템이 없다면
            print("Item Not Found")
            return
        else:
            self.delete_node(p=p,removed=removed)
            
    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            link = curr.link
            curr.link = prev
            prev = curr	
            curr = link	
        self.head = prev
       
            
            
        

L = LinkedList()                            #객체 
while True:
    cmd = input()
    if cmd == "exit":
        break
    elif cmd == "print":
        L.print_list()
    elif cmd == "reverse":
        L.reverse()
    else:
        cmd, param = cmd.split()
        if cmd == "ins_first":
            L.insert_first(int(param))
        elif cmd == "ins_last":
            L.insert_last(int(param))
        elif cmd == "find":
            node = L.search(int(param))
            if node is None: print('Item Not Found')
            else: print("{} Found".format(node.item))
        elif cmd == "del":
            L.delete(int(param))
