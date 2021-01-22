## 양방향 연결리스트 by 값으로 찾기
# 작성자: 이종은

class Node:
  def __init__(self, element): 
    self.element = element 
    self.next = None 
    self.previous = None 

class DoublyLinkedList: 
  def __init__(self): 
    self.head = Node('head') 
    
  def find(self, item): 
    cur_node = self.head 
    while cur_node.element != item: 
      cur_node = cur_node.next 
    return cur_node 
    
  def insert(self, item, new): 
    new_node = Node(new) 
    cur_node = self.find(item) 
    new_node.next = cur_node.next 
    cur_node.next = new_node 
    new_node.previous = cur_node 
    
  def show(self): 
    cur_node = self.head 
    while cur_node.next is not None: 
      print(cur_node.element, end=' -> ') 
      cur_node = cur_node.next 
    print(cur_node.element)

  def remove(self, item): 
    cur_node = self.find(item) 
    cur_node.previous.next = cur_node.next 
    cur_node.previous = None 
    if cur_node.next is not None: 
      cur_node.next.previous = cur_node.previous 
      cur_node.next = None 
      
  def find_last(self): 
    cur_node = self.head 
    while cur_node.next is not None: 
      cur_node = cur_node.next 
    return cur_node 
    
  def show_reverse(self): 
    cur_node = self.find_last() 
    while cur_node.previous is not None:
       print(cur_node.element, end=' <- ') 
       cur_node = cur_node.previous 
    print(cur_node.element) 
    
boo = DoublyLinkedList() 
boo.insert('head', '1') 
boo.insert('1', '2') 
boo.insert('2', '3') 
boo.insert('3', '4') 
boo.show() 
boo.remove('4') 
boo.show() 
print(boo.find_last().element) 
boo.show_reverse()



## 양방향 연결리스트 by 위치로 찾기
# 작성자: 이종은

class Node: 
  def __init__(self, data): 
    self.data = data 
    self.next = None 
    self.previous = None 
    
class DblLinkedList: 
  def __init__(self): 
    self.head = Node('head')
    self.list_size = 0
    
  def find(self, pos): 
    cur_node = self.head        
    cnt = 0
    while cnt < pos:             
      cur_node = cur_node.next  
      cnt += 1 
    return cur_node              
    
  def insert(self, pos, data): 
    new_node = Node(data)           # 신규 노드 생성
    cur_node = self.find(pos)       # pos 위치 이전 노드  

    if self.list_size == 0 or pos == self.list_size: # 삽입 될 위치가 맨끝인 경우
      new_node.previous = cur_node  # 신규노드.prev = 이전노드
      cur_node.next = new_node      # 이전노드.next = 신규노드

    else: 
      new_node.previous = cur_node       # 신규노드.prev = 이전노드
      cur_node.next.previous = new_node  # 이전노드.next.prev = 신규노드
      new_node.next = cur_node.next      # 신규노드.next = 이전노드.next
      cur_node.next = new_node           # 이전노드.next = 신규노드     

    self.list_size += 1

  def remove(self, pos): 
    cur_node = self.find(pos)
    if cur_node.next.next == None:
      cur_node.next = None
    else:
      cur_node.next.next.previous = cur_node
      cur_node.next = cur_node.next.next
    self.list_size -= 1

  def replace(self, pos, data):
    cur_node = self.find(pos)            # pos 위치의 이전 노드
    new_node = Node(data)                # 신규 노드 생성

    if cur_node.next.next ==  None:      # 대체될 노드의 위치가 맨끝인 경우
      new_node.previous = cur_node       # 신규노드.prev = 이전노드
      cur_node.next = new_node           # 이전노드.next = 신규노드

    else :  
      new_node.previous = cur_node            # 신규노드.prev = 이전노드
      cur_node.next.next.previous = new_node       # 이전노드.next.prev = 신규노드
      new_node.next = cur_node.next.next      # 신규노드.next = 이전노드.next.next
      cur_node.next = new_node                # 이전노드.next = 신규노드

  def find_last(self): 
    cur_node = self.head 
    while cur_node.next is not None: 
      cur_node = cur_node.next 
    return cur_node 
    
  def size(self):
    return self.list_size
    
  def display(self): 
    if self.size()==0:
      print("[단순연결리스트 항목 수= 0] : ")
    else:
      print("[단순연결리스트 항목 수= {}] : ".format(self.size()), end="")
      cur_node = self.head.next                       # 현재노드 = head.next 부터 
      while cur_node.next != None:                    # next가 노드일때까지
        print("<{}>".format(cur_node.data), end=" ")  
        cur_node = cur_node.next                      # 현재노드 = 현재노드.next
      print("<{}>".format(cur_node.data))            
       
  def reverse(self): 
    if self.size()==0:
      print("[단순연결리스트 항목 수= 0] : ")
    else:
      print("[단순연결리스트 항목 수= {}] : ".format(self.size()), end="")
      pos = self.list_size
      cur_node = self.find(pos)
      while cur_node.data != "head":                    #  노드일때까지
        print("<{}>".format(cur_node.data), end=" ")  
        cur_node = cur_node.previous                 # 현재노드 = 현재노드.
      print()

  def clear(self):
    while self.list_size != 0:
      self.remove(0)

list1 = DblLinkedList() 
list1.insert( 0, 10) 
list1.insert( 0, 20) 
list1.insert( 1, 30) 
list1.insert(list1.size(), 40)
list1.insert(2, 50) 
list1.display() 

list1.remove(2) 
list1.remove(list1.size()-1)
list1.remove(0)  
list1.replace(1, 90) 
list1.display()

list1.clear() 
list1.display()