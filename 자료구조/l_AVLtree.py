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
        if self.root = z:
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
        z.parent x
        
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
# AVL tree: 자식 부트리 간의 높이 차 <= 1

class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.height = -1 # 존재하지 않는 노드의 높이를 -1이라 하자.
        # 높이는 max(leftHeight, rightHeight) + 1 인데,
        # 자식 노드가 없는 노드의 높이를 0(-1 + 1)으로 올바르게 계산할 수 있어 make sense.
    
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
            return -1 # 노드 클래스 부분에서 설명한 것과 상통.
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
        z.parent x
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
        if self.root = z:
            self.root = x
        z.height = max(self.height(z.left), self.height(z.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def bF(self, v): # Balance Factor
        return self.height(v.left) - self.height(v.right)    

    def isBalanced(self, v):
        return bf(v) <= 1

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
            self.bF(z.right) > 0: # z 불균형의 right-left case
                z.right = self.rotateRight(z.right)
            z = self.rotateLeft(z)
        elif self.bF(z) > 1:
            if self.bF(z.left) < 0: # left-right case
                z.left = self.rotateLeft(z.left)
            z = self.rotateRight(z)

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
        p = self.findLocation(key)
        if p != None and p.key == key:
            print("The key is already in use.")
            return p
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
            v.height = max(self.height(z.left), self.height(z.right)) + 1
            while w != None:
                w = v
                if not self.isBalanced(w):
                    self.rebalance(w)
                w = v.parent
                if w.parent == None:
                    self.root = w


    # 좀 더 복잡?
    # 균형이 깨진 곳 맞추면
    # 그 위 부모 노드에서 균형 안 맞을 수 있음
    # 계속 올라가면서 균형 맞추고 루트 노드까지
    균형 맞추면 계속 파급 효과 발생해서
    worst case에 최악 O(log n) rotations
    높이만큼 로테이션 할 수 있음 최악의 경우 insert와 다르게
    def delete(self, u): # u라는 노드를 지운다 하면
        v = super(AVLtree, self).deleteByMerging(u)
        # v는 u를 지우고 u의 부모를 return한 것
        # p = v 그림이 오류 p = v
        # delete에서
        # BST와 다르게 return 해줘야 할 게 뭐냐면 이것
        # 지움으로써 균형이 깨질 가능성이 있는 가장 깊은 곳에 있는
        while v != None:
            if v is not balanced:
                z = v # 밸런스가 깨지면 바로 그 v가 z
                if z.left.height >= z.right.height:
                    y = z.left
                else: y = z.right

                if y.left.height >= y.right.height:
                    y = y.left
                else: x = y.right
                v = rebalance(x, y, z) # z, y, x의 경우에 따라 한 번 rot 하거나 두 번 rot
            w = v
            v = v.parent # 강의 그림과 다름
                # v
                #   w
                # 새로 올라간 v가 균형 깨졌으면 다시 while 돌아가서
                # v가 z가 되고
        # while만 다 빠져 나오면 v == None
        # w는 v의 바로 직전 자식 노드니까 w == root
        self.root = w
        O(log n) # log n 높이 만큼 올라가서 상수 걸리는 회전 매 레벨 해줌

    
    


    def insert(self, key):
        10
    5      15
       7
          9
        9라는 게 들어오면서 5가 균형이 깨짐.
        리밸런스 해줘야.
        균형하는 z가 존재한다면 리밸런스 해줘야
        rebalance(x, y, z)
        5 7 9  z y x

        경우 두 가지 -> 1회 rot 경우 or 2회 rot 경우
    def insert(self, key): 
        1. v = super(AVLtree, self).insert(key) O(log n)
        2. find x, y, z(처음으로 AVL 조건 깨진 노드) v노드로부터 위로 올라가면서 x,y,z 찾아야 함 높이 h만큼 고작 O(h)
        x가 들어오면서 z가 깨짐. 이걸 균형 맞춰주기 위해
        3. w = rebalance(x, y, z) (w는 원래 z 위치에 있었던 노드, 리밸런스 한 후 그 노드를 돌려줌 return. 루트 노드가 하필이면 루트 노드였을 수 있으니까 z가 원래 루트였지만 새로운 노드가 새로운 루트가 될 수 있으니 그것을 반영)
        O(1)
        4. if w.parent == None:
                self.root = w
        O(1)

        총 수행 시간은 O(log n)
BST 손 봐야 하니까 그냥 상속 받지 말고 새로 해도 될 거 같은데.
상속하면 init 없어도 됨.

    