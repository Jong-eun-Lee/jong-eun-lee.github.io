## Heap(힙) (max heap - 부모 노드의 key가 자식 노드의 key보다 크거나 같음)
# 작성자: 이종은

# 트리 표현법
#     a
#    / \ 
#   b   c
#  / \ / \
#    d e

# 표현법 1: 리스트: level 0 -> level 1 -> ...
# A = [a, b, c, None, d, e]
# level 0은 A[0], level 1은 A[1]과 A[2]
# A[k]의 왼쪽 자식 노드 인덱스는 A[2*k+1]
# A[k]의 부모 노드 인덱스는 A[(k-1)//2]
# 상수 시간에 자식 노드와 부모 노드를 알 수 있음. O(1).
# 중간에 없는 노드를 모두 None으로 표시하여 메모리 낭비가 있을 수 있음(Heap의 경우 중간에 None이 없이 다 채움).


# 표현법 2: 리스트(재귀적):
# A = [a, [a의 왼쪽 부트리(subtree)], [a의 오른쪽 부트리]]
# = [a, [b, [], [d, [], []]], [c, [e, [], []]]]

# 표현법 3: 노드 class(직접 정의)
# key 값, 자식 노드 가리키는 링크 두 개(left와 right), 부모 노드 가리키는 링크(parent) 등 최소 4개 갖는 노드 class 정의

# Heap을 첫 번째 표현법을 이용하여 구현해본다.
# Heap의 조건은 다음과 같다.
#           21
#         /    \
#        13     6
#       / \    / \
#      11  7  5   2
#     /
#    1
# 1. 모양 조건: 완전 이진 트리 형태여야 한다(마지막 레벨은 노드가 빠짐없이 존재하지 않아도 되지만, 왼쪽부터 차례대로 채워져야 함).
# 2. 값 조건: 모든 부모 노드의 key 값은 자식 노드의 key 값보다 작지 않다.
# heap의 루트 노드는 가장 큰 값을 가짐.(=A[0] 가장 큼).
# 제공 연산: 1. insert (O(log n)) 2. find-max: return A[0] O(1) 3. delete-max: maximum을 지우고 나머지들을 heap을 유지해도록 해야. (O(log n))
# makeHeap 연산도 필요(삭제나 인서트 후에? 힙 값 조건 만족하도록 하는 것).
# makeHeap 연산에는 heapifyDown이 필요?
# heapifyDown(가장 마지막에 있는 인덱스부터 루트 노드까지 숫자를 밑으로 내려보냄)
# 리프노드는 신경 안 쓰고 자식 노드 있는 거 보는데
# 만약에 두 자식 노드보다 부모 노드가 작다면 두 자식 노드 중 큰 걸로 부모 노드와 교체.
#

class Heap:
    def __init__(self, L=[]):
        self.A = L
    
    def __str__(self):
        return str(self.A)
    
    def __len__(self):
        return len(self.A)

def makeHeap(self): # 힙의 갑 조건 만족하도록 리스트 값 재배열
    n = len(self.A)
    for k in range(n-1, -1, -1): # k = n-1, n-2, ..., 0 배열의 마지막부터
        # A[k]를 heap 성질이 만족하는 곳으로 내려 보냄
        self.heapifyDown(k, n) # k는 A[k]를 밑으로 내려보라는 것. n은 A에 들어있는 힙에 원소 개수
    # n번 heapify down을 호출. O(n*heapifydown의 수행 시간) = O(n*h(heap 높이)) = O(n*log n)

def heapifyDown(self, k, n): # A[k]를 중심으로 그 밑에 heap 성질 되게 (A[k]의 부트리 검사하는 거 같음)
    # A[k], n은 힙의 전체 노드 수
    # A[k]와 왼쪽, 오른쪽 자식을 비교하여 heap 성질 만족하게 배열
    while 2*k + 1 < n:  # A[k]가 리프 노드가 아니면
        left, right = 2*k/ + 1, 2*k + 2
        if left < n and self.A[left] > self.A[k]:
            max = left
        else:
            max = k
        
        if right < n and self.A[right] > self.A[max]:
            max = right
        
        if max != k:
            self.A[k], self.A[max] = self.A[max], self.A[k]
            k = max # 자식과 바꿨다면 k는 밑으로 내려감
        else: # 자식보다 큰 경우 부모 노드가
            break
    # 루트에 있는 걸 heapifyDown 하는 게 제일 오래 걸릴 것.
    # 이게 최악일 것인데, -> 루트부터 리프까지의 높이가 그것일 것
    # heap의 높이만큼이 최악 h=힙 높이
    # O(h)만큼 걸림

# n개의 노드를 갖고 있는 힙의 높이 h
# 마지막 레벨은 레벨 h
# h-1 레벨의 노드 개수는 2^(h-1)
# h 레벨에 다 채워지지 않는다면 노드 개수가 < 2^(h)
# 마지막 레벨 최소 한 개이므로
# 1+2+2^2+...+2^(h-1)+1 <= n (레벨이 h인 힙의 전체 노드 수)
# (2^h - 1)/(2 - 1) + 1 = 2^h <= n
# h <= log2 n
# n개의 노드를 갖고 있는 heap의 높이 h는 아무리 커봤자 log n을 넘지 못한다.
# heapifyDown의 수행시간은 결국 O(h) = O(log n)
# 그래서 makeHeap의 수행시간은 O(n*log n)인데,
# 최악이 아닌 경우 리프 노드에 가까운 레벨에서 heapifyDown할 수도 있기 때문에 O(n * log n)이 아닌 O(n)까지 줄어들 수도 있음.

    # 가장 큰 걸 맨 오른쪽으로 보내고
    # 루트노드부터 히피파이 다운하면
    # 두 번째로 큰 게 맨 오른쪽에서 두 번째로 가고
    # 해서 오름차순으로 
    def heapSort(self):
        n = len(self.A)
        for k in range(len(self.A)-1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0] # 지우진 않고 자리만 바꿈
            n = n-1
            self.heapifyDown(0, n)
    # O(n*log n)
    
    # insert는 리스트의 마지막에 넣은 후 힙 성질 만족하도록 위에 올리면서
    def insert(self, key):
        self.A.append(key)
        k는 마지막 인덱스
        self.A.heapifyUp(k)
    # heapifyUp이 O(log n) 시간이라 insert도
    # insert n번 해서 힙 만들면 O(n*log n)인데
    # makeHeap으로 O(n)만에 하는 게 더 나음

    def heapifyUp(self, k):
        while k > 0 and self.A[(k-1)//2] < self.A[k]: # 인덱스가 루트 노드 도달 전까지
            self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
            k = (k-1)//2
    # 최악의 경우 루트 노드까지. 상수 시간 걸림 h = O(log n)
    # log n 시간 걸림

    def findMax(self):
        return self.A[0]
    # O(1)

    def deleteMax(self):
        # 루트 노드 제거 후 힙의 모양을 위해 맨 마지막에 있는 걸 루트 노드에.
        # 이제 루트 노드에 있는 것을 힙 성질 만족하도록 내려가게 하면서 재배열
        if len(self.A) == 0:
            return None
        key = self.A[0]
        self.A[0], self.A[len(A)-1] = self.A[len(A)-1], A[0]
        self.A.pop()
        self.heapifyDown(0, len(A)) # 이때 n은 루트 노드 제거 전보다 하나 더 적음 pop해서 이게 반영 됐을 것
        return key
    # O(log n)

    # search 함수는 없음 search를 효율적으로 하기 위한 자료구존느 없음
    # insert, deleteMax에 특화된 application에 쓰임.
    # osr
