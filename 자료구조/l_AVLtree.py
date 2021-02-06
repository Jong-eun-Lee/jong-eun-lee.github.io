## AVL Tree
# 작성자: 이종은

#===========================================================================================#
## Balanced BST (균형 이진 탐색 트리)
# 작성자: 이종은
# 이진 탐색 트리의 높이 범위는 log(n+1) - 1 <= h <= n-1 과 같은데,
# 조정 등을 통해 n개의 노드가 저장된 BST의 h를 항상 O(log n)으로 유지하는 것이
# '균형 이진 탐색 트리(balanced binary search tree)'

# 삽입, 삭제 연산 등을 통해 트리의 높이가 높아지면 O(log n)을 유지하기 위한 조정이 필요하다.
# 조정은 Rotation(회전)을 통해 이루어진다(한 번 혹은 여러 번의 회전을 통해).
# ex) z 입장에서 x의 왼쪽 부트리 A의 높이가 높으면 right rotation을 통해 조정.
#      z
#    x   C
#  A  B
# A < x < B < z < C (이 성질을 유지하면서 회전해야 함)
#    z's parent
#              x
#            A   z
#               B  C
# z를 기준으로 right rotation 하면 (right rotation at z)
# z는 오른쪽으로 내려가고 x가 위쪽으로. B은 x가 아닌 z에 붙음.
# x와 A는 올라가면서 한 레벨 줄어듦
# z와 C는 내려가면서 한 레벨 늘어남.
# B는 똑같은 레벨.

# x는 B 버리고 z를 자식으로 삼고 z는 B를 새로운 자식으로 삼는다.
# x와 z.parent와의 관계, x와 z와의 관계, z와 B와의 관계 갱신
# z.parent.child = x
# x.parent = z.parent
# x.right = z
# z.parent = x
# z.left = B
# B.parent = z
# 이것을 다시 left rotation 해주면 원래 모양대로 돌아간다.

def rotateRight(self, z):
    if z == None: return
    x = z.left
    if x == None: return
    b = x.right

    x.parent = z.parent
    if z.parent:
        if z.parent.left == z:
            z.parent.left = x
        else:
            z.parent.right = x
    x.right = z
    z.parent = x
    z.left = b
    if b:
        b.parent = z
    if z == self.root:
        self.root = x
    # height에 대한 정보를 가지는 클래스를 이용한다면
    # x와 z의 height 값을 update 해줘야 한다.

def rotateLeft(self, z):
    if z == None: return
    x = z.right
    if x == None: return
    b = x.left

    x.parent = z.parent
    if z.parent:
        if z.parent.left == z:
            z.parent.left = x
        else:
            z.parent.right = x
        
    x.left = z
    z.parent = x
        
    z.right = b
    if b: b.parent = z

    if z == self.root:
        self.root = z
#===========================================================================================#

## AVL Tree (Adelson-Velsky & Landis, 1962)
# 모든 노드에 대해서 노드의 왼쪽 부트리와 오른쪽 부트리의 높이 차가 1이하인 BST
# 그러면 이 조건을 만족하면 항상 높이가 O(log n)이 되는가?
# 증명(높이가 h이고 노드 개수가 n인 AVL tree가 h <= c*(log2 n) 임을):
# h = 0 최소 노드 수 1
# h = 1 최소 노드 수 2
# h = 2 최소 노드 수 4
# h = 3의 최소 노드 수 예시 (4 + 2 + 1)
#        o
#     o     o
#   o  o   o
# o 
# 루트 노드의 왼쪽엔 높이가 2인 최소 노드의 AVL tree가 붙고,
# 루트의 오른쪽엔 높이가 1인 최소 노드의 AVL tree가 붙어 있다.


# 높이가 h인 AVL tree 중 최소 노드 개수를 Minh라고 하면
# Min0 = 1
# Min1 = 2
# Min2 = 4
# Min3 = 7
# Min4 = 12
# Minh = 1 + Min(h-1) + Min(h-2) > 1 + 2*Min(h-2)
# > 2*Min(h-2) = 2*(1+ Min(h-3) + Min(h-4))
# > 2*(2*Min(h-4)) = 2^2(Min(h-4))
# > 2^(h/2) * Min0 # Min 0까지 가려면 2를 h/2번 빼줌 (h가 짝수일 때)
# = 2^(h/2)
# ∴ Min(h) >= 2^(h/2)

# 2^(h/2) <= Minh <= n
# h/2 <= log2 n  
# h <= 2 * log n
# ∴ h = O(log n)


class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.height = -1
        # 존재하지 않는 노드의 높이를 -1로 할 경우
        # 자식 노드가 없는 노드의 높이를 max(-1, -1) + 1. 즉 0으로 계산할 수 있어 make sense.
    
    def __str__(self):
        return str(self.key)

# AVL 조건: abs(leftHeight - rightHeight) <= 1
class AVLtree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def height(self, v):
        if v == None:
            return -1
        return v.height

    #  z.p     =>    z.p
    #   z      =>     x
    # a   x    =>   z   c
    #    b c   =>  a b
    def rotateLeft(self, z):
        if z == None: return
        x = z.right
        if x == None: return
        b = x.left
        x.parent = z.parent
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        x.left = z
        z.parent = x
        z.right = b
        if b: b.parent = z
        if z == self.root:
            self.root = z
        z.height = max(self.height(z.left), self.height(z.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x # z 자리에 올라온 x return

    def rotateRight(self, z):
        if z == None: return
        x = z.left
        if x == None: return
        b = x.right
        x.parent = z.parent
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        x.right = z
        z.parent = x
        z.left = b
        if b:
            b.parent = z
        if z == self.root:
            self.root = x
        z.height = max(self.height(z.left), self.height(z.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def bF(self, v): # Balance Factor
        return self.height(v.left) - self.height(v.right)
        
    def isBalanced(self, v):
        return abs(self.bF(v)) <= 1

    # rebalance case는 총 네 가지(z가 unbalanced 하다고 하자).
    # right-right case solved by "rotateLeft at z"
    #     z            ->       y
    #  T1    y         ->    z      x
    #     T2   x       ->  T1 T2  T3 T4
    #        T3 T4     ->
    # (left-left case는 rotateRight로 해결)
    # right-left case solved by rotateRight at y and "rotateLeft at z"
    #      z       ->        z             ->       x
    #  T1     y    ->    T1      x         ->   z      y
    #       x  T4  ->         T2    y      -> T1 T2  T3 T4
    #     T2 T3    ->             T3  T4   ->
    # (left-right case는 rotateLeft at y 후 rotateRight at z로 해결)
    def rebalance(self, z):
        if self.bF(z) < -1: # z의 오른쪽 부트리 높이가 큰 불균형
            if self.bF(z.right) > 0: # z 불균형의 right-left case
                z.right = self.rotateRight(z.right)
            w = self.rotateLeft(z)
            return w
        elif self.bF(z) > 1:
            if self.bF(z.left) < 0: # left-right case
                z.left = self.rotateLeft(z.left)
            w = self.rotateRight(z)
            return w
        else: return

    def findLocation(self, key):
        if self.size == 0:
            return None
        v= self.root
        p = None
        while v != None:
            if v.key == key:
                return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p

    def search(self, key):
        v = self.findLocation(key)
        if v and v.key==key:
            return v
        else:
            return None

    def insert(self, key):
        v = self.forInsert(key)
        while v != None:
            if not self.isBalanced(v): # v가 불균형이면
                z = v
                if self.bF(z) > 0: # z의 부트리의 높이가 더 큰 쪽을 y로 함.
                    y = z.left
                else: y = z.right
                if self.bF(y) > 0:
                    x = y.left
                else: x = y.right
                v = self.rebalance(z)
            w = v
            v = v.parent
            if v == None:
                self.root = w

    def forInsert(self, key):
        p = self.findLocation(key)
        if p != None and p.key == key:
            print("The key is already in use.")
            return
        else:
            v = Node(key)
            if p == None:
                self.root = v
            else: # p.key != key
                v.parent = p
                if p.key > key:
                    p.left = v
                else:
                    p.right = v
            self.size += 1
            v.height = max(self.height(v.left), self.height(v.right)) + 1
            return v

    def delete(self, u):
        v = self.deleteByCopying(u) # v는 지워낸 u의 parent
        while v != None:
            if not self.isBalanced(v): # v가 불균형이면
                z = v
                if self.bF(z) > 0: # z의 부트리의 높이가 더 큰 쪽을 y로 함.
                    y = z.left
                else: y = z.right
                if self.bF(y) > 0:
                    x = y.left
                else: x = y.right
                v = self.rebalance(z)
            w = v
            v = v.parent
            if v == None:
                self.root = w

    def deleteByCopying(self, x):
        if x == None: return
        l, r, p = x.left, x.right, x.parent
        if l == None:
            replace = r
        else:
            m = l
            while m.right:
                m = m.right
            m.parent.right = m.left
            if m.left:
                m.left.parent = m.parent
            m.right = r
            m.left = l
            l.parent = m
            if r:
                r.parent = m
            replace = m            
        if self.root == x:
            if replace:
                replace.parent = None
            self.root = replace
        else:
            if p.left == x:
                p.left = replace
            else:
                p.right = replace
            if replace:
                replace.parent = p
        self.size -= 1
        if p:
            p.height = max(self.height(x.left), self.height(x.right)) + 1
        return p

    def preorder(self, v):
        if v != None:
            print(v.key, end=" ")
            self.preorder(v.left)
            self.preorder(v.right)
    
    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=" ")
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=" ")

a = AVLtree()
a.insert(25)
a.insert(5)
a.insert(53)
a.insert(1)
a.insert(6)
a.insert(27)
a.insert(67)
a.insert(26)
a.insert(28)
a.insert(29)
a.insert(30)
a.delete(a.search(30))

a.preorder(a.root)
print()
a.inorder(a.root)
print()
#      25          =>         25
#     /   \        =>        /  \
#    5    53       =>       5   28
#   / \   / \      =>      /\    /\
#  1  6  27 67     =>     1  6  27 53
#       / \        =>          /    /\
#      26 28       =>         26   29 67
#           \
#           29
### 문제점 1: 오른쪽 결과가 아닌 왼쪽으로 나옵니다.

print(a.height(a.root))
### 문제점 2: 높이가 정상적으로 계산이 안 됩니다.

print(a.isBalanced(a.root))
### 문제점 3: isBalanced가 유효하지 않습니다.