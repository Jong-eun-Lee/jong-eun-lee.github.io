## Balanced BST (균형 이진 탐색 트리)
# 작성자: 이종은
# log(n+1) <= h <= n-1
# 조정을 통해서 트리의 h를 항상 O(log n)으로 하는 이진 탐색트리
# -> balanced binary search tree
# n개의 노드가 저장된 BST 중에서 그 높이가 O(log2 n)에 비례하는 정도로 유지하는 게 '균형'
# 높이를 O(log n)으로 유지하려고 조정함.

# 그 조정이 Rotation(회전) 트리 일부를 회전시켜서 전체 트리의 높이 줄임
#      z
#    x   C
#  A  B
# A <= x < B < z < C

# z를 기준으로 right rotation 하면
# right rotation at z
# z는 오른쪽으로 내려가고 x가 z쪽으로
#
#       z's parent
#             x
#            A   z
#               B  C
# x는 한 레벨 위, z는 한 레벨 아래 A는 전체적으로 한 레벨 위
# B 그대로. C는 한 레벨 내려옴
# x와 A는 올라가면서 한 레벨 줄어듦
# z와 C는 내려가면서 한 레벨 늘어남.
# B는 똑같은 레벨.
# right rotation(z 입장에서 왼쪽 서브트리가 높이가 크면 해줌)

# z.parent.child = x
# x.parent = z.parent
# x.right = z
# z.parent = x
# z.left = b
# b.parent = z
# 6개 바꿔야.


# 왼쪽이 무거우면 right rotation
# rotation은 한 번 또는 여러 번 해서 높이 조정
# 두 번째 걸 left rotation 해주면 첫 번째 걸로 돌아감.

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
    
    def rotateLeft(self, z):


# AVLtree
# 모든 노드에 대해서 
# 노드의 왼쪽 부트리와 오른쪽 부트리의 높이 차가 1이하인 BST
# 그러면 이 조건을 만족하면 항상 높이가 O(log n)이 되는가?
# 증명:
# h = 0 최소 노드 수 1
# h = 1 최소 2
# h = 2 최소 4
# h = 3 AVL 중 노드 최소인 경우 최소니까 높이 차이는 1이어야.
#       o
#     o   o
#   o  o o
# o 
# 루트 노드의 왼쪽엔 높이가 2인 최소 노드의 AVL tree가 붙어야 하고
# 루트의 오른쪽엔 높이가 1인 최소 노드의 AVL tree가 

# 높이가 h인 AVL tree 중 최소 노드 개수를 Minh라고 하면
# Min0 = 1
# Min1 = 2
# Min2 = 4
# Min3 = 7
# Minh = 1 + Min(h-1) + Min(h-2) >= 1 + 2*Min(h-2) 
# >= 2*Min(h-2) = 2*(1+ Min(h-3) + Min(h-4))
# >= 2*(2*Min(h-4)) = 2^2(Min(h-4))
# >= 2^(h/2) * Min0 # Min 0까지 가려면 2를 h/2번 빼줌 (h가 짝수일 때)
# = 2^(h/2)
# Min(h) >= 2^(h/2)

# 높이 h이고 노드 개수 n인 AVL tree가
# h <= c*(log2 n) 임을 증명해야

# 2^(h/2) <= Minh <= n
# h/2 <= log2 n 
# h <= 2 * log2 n
# ∴ h = O(log n)

# AVL tree: 자식 부트리의 높이 차 <= 1

class Node: # BST와 동일. key, left, right, parent
# AVL tree는 높이 정보 있어야
# height라는 멤버 변수 추가해야

class BST: # 사용 (insert, deleteByMerging, deleteByCopying, search)
# insert와 delete 할 때 height 변경될 수 있는데
# height 정보가 변화함을 update 돼야 함.

class AVLtree(BST): # BST 클래스 상속. BST의 하위 클래스. 모든 어트리뷰트 멤버변수, 메소드 등 다 물려 받아서 쓸 수 있음. 
    # Adelson-Velsky & Landis (1964) 가장 오래된 균형 이진 탐색 트리
    