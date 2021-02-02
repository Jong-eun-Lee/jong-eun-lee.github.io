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
# h <= 2 * log2 n
# ∴ h = O(log n)
# AVL tree: 자식 부트리 간의 높이 차 <= 1

class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0 # BST와 다르게 height에 대한 정보 추가
    
    def __str__(self):
        return str(self.key)

    def leftHeight(self):
        return self.left.height if self.left is not None else 0
    
    def rightHeight(self):
        return self.right.height if self.right is not None else 0



class BST: # 사용 (insert, deleteByMerging, deleteByCopying, search)
# insert와 delete 할 때 height 변경될 수 있는데
# height 정보가 변화함을 update 돼야 함.

class AVLtree(BST): # BST 클래스 상속. BST의 하위 클래스. 모든 어트리뷰트 멤버변수, 메소드 등 다 물려 받아서 쓸 수 있음. 
    # Adelson-Velsky & Landis (1964) 가장 오래된 균형 이진 탐색 트리
    