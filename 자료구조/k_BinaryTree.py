## Binary Search Tree(BST)(이진 탐색 트리)
# 작성자: 이종은
# 탐색 -> 이진 트리의 어떤 key 값들을 여러 개 저장 후
# 어떤 key 값들이 있는지 search하는 연산 많이 하는데
# search를 효율적으로 할 수 있도록 잘 조직화된 것이 이진 '탐색' 트리
# ! 각 노드 왼쪽 부트리의 key 값은 노드의 key 값보다 작거나 같다.
# ! 각 노드 오른쪽 부트리의 key 값은 노드의 key 값보다 크거나 같아야 한다.
# (key는 서로 다르기 때문에 같진 않을 것)
# search(19)를 한다 하면 루트 노드의 15와 비교
# 루트 노드보다 크니까 오른쪽 서브트리 찾으러 감
# 탐색하는데 모든 걸 샅샅이 뒤지는 게 아니라
# 규칙에 따라 왼쪽 부트리 향할지 오른쪽 부트리 향할지 이중택일
# search는 O(h). 이진 탐색 트리의 높이를 최대한 작게 할수록 탐색이 효율적이게 될 것임.

class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.key)

# 깊이: 루트 노드에서 해당 노드까지의 경로 길이
# 높이: 해당 노드에서 자손노드까지의 가장 길이가 긴 경로의 경로길이
# 트리의 높이 = 루트 노드의 높이
    
# traversal(순회) 1. preorder traversal 2. inorder traversal 3. postorder traversal
# 자기 자신을 M, 왼쪽 부트리를 L, 오른쪽 부트리를 R이라고 하면 # 1. preorder: MLR(M이 앞에) # 2. inorder: LMR(M이 가운데에) # 3. postorder: LRM(M이 마지막에)
# L을 R보다 먼저 방문하는 게 공통점. 부트리에 들어갈 때는 재귀적으로 다시 order를 따름.
#     A
#    / \
#   B   C
#  /\    \
# D  E    F
#   /\    /
#  G  H  I
# postorder(전위): A B D E G H C F I
# inorder(중위): D B G E H A C I F
# postorder(후위): D G H E B I F C A

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__() # Node class에 iter가 선언 돼 있어야.
        # iter는 inorder라든지로.  yield?

    def preorder(self): # 현재 방문 중인 노드 = self
        if self != None:
            print(self.key, end=" ")
            if self.left != None:
                self.left.preorder()
            if self.right != None:
                self.right.preorder()
    
    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=" ")
            self.inorder(v.right)

    def postorder(self):
        if self != None:
            if self.left != None:
                self.left.inorder()
            if self.right != None:
                self.right.inorder()
            print(self.key, end=" ")

    def findLocation(self, key): # key 값에 해당하는 노드가 있다면 return. 없다면 그 노드가 삽입될 '부모 노드'를 return.
        if self.size == 0:
            return None # 루트 노드 자리에 들어가야 하는데, 루트 노드 부모가 None이므로. 
        v= self.root
        p = None # p는 v의 parent
        while v != None:
            if v.key == key:
                return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p # 부모 노드를 return
    # O(h)

    def search(self, key):
        v = self.findLocation(key)
        if v == None:
            return None
        else:
            return v
    # O(h)

    def insert(self, key):
        p = self.findLocation(key)
        if p == None or p.key != key:
            v = Node(key)
            if p == None: # = 들어갈 key 자리가 루트 노드란 것 (루트 노드의 p는 None)
                self.root = v
            else: # p가 None이지만, p의 key 값이 삽입하려는 key 값과 다르다는 것 (key 값이 같다는 건 중복됐다는 것. 아무 것도 안 해도 됨.)
                v.parent = p
                if p.key >= key:
                    p.left = v
                else:
                    p.right = v
            self.size += 1
            return v
        else:
            print("key is already in tree")
            return p # p는 None
            # 새로 insert 된 노드는 리프 노드로 있어도 되는 것
    # findLocation이 O(h)이니 insert도 O(h)

    # 삭제연산 merging으로 하는 것과 copying 하는 것 두 개
    
    #
    def deleteByMerging(self, x): # 노드 x를 삭제 # x 자리에 L이 오도록 한 뒤 L의 가장 큰 노드의 오른쪽 자식에 R을 붙임.
        # 어떤 부분을 없애 버리면 그 노드의 자식 노드가 있었다면 형태가 불완전해질 수도
        # 없앤 부분에 없앤 노드의 왼쪽 부트리 전체를 그대로 갖다 넣음.
        # 오른쪽 부트리의 첫 노드는 왼쪽 부트리의 가장 큰 key를 가진 노드에 오른쪽 child로 이어져야.
        # L's key < R's key 니까
        # L의 max는 오른쪽 자식 노드를 계속 따라 내려가서 찾음.

        # 몇 가지 특별한 경우들을 살펴 보자.
        # 1. L의 루트 노드 a == None이라면 x 자리에 R이 와야
        # 2. x == root 라면 root를 업데이트 해줘야 함.

        a = self.x.left
        b = self.x.right
        pt = self.x.parent
        c = x자리를 대체할 노드
        m = L에서 가장 큰 노드가

        if a == None: # a가 None이면 L이 없
            b를 x 자리에
        if a != None:
            c = a
            m = a
            while m.right:
                m = m.right
            if b != None:
                b.parent = m
                m.right = b
        else: # a == None
            c = b
        
        if pt != None:
            if c:
                c.parent = pt
            if pt.key < c.key:
                pt.right = c
            else:
                pt.left = c
        else: # x는 root였는데, 지운 것
            self.root = c
            if c: # c가 None이 아니라면
                c.parent = None
        self.size -= 1
        return
    # O(h) m을 찾는 데 시간이 제일 많이 걸림 카핑도.
    
    def deleteByCopying(self):
        # x를 지우고 L의 가장 큰 노드를 m으로 하여 x 자리에 m을 카피
        # m은 계속 오른쪽 자식 계속 찾아 내려감
        # m이 있던 자리에 m의 왼쪽 서브트리가 와서
        # m의 parent의 오른쪽 자식으로 옴
        # m의 오른쪽 자식은 없어요 왜냐하면 L에서 가장 큰 값이 m이니까
    # O(h)
                
            
             
    



                
        v = Node(key) # v는 p의 자식으로 그 자리에
        self.size += 1
        
    # 연산들이 O(h)이니 높이가 중요
    # 높이 등의 조건을 강제적으로 유지하도록 하는 것을 balanced binary search tree
    
