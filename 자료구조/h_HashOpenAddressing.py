### Hash Table 구현
## Open Addressing - Linear Probing
# 작성자: 이종은

### 충돌 회피 방법(Collision Resolution Method)의 대표적 방법은 Open addressing과 Chaining.
## open addressing -> 충돌할 경우 다른 빈칸을 찾아 저장시키는 것. 한 slot당 들어갈 수 있는 entry가 하나.
# open addressing에는 linear probing, qudratic probing, double hashing 등이 있다.

# Linear Probing - 충돌이 일어나면 거기서 밑으로 고정된 이동폭에(선형적) 따라 (예를 들어 한 칸씩) 탐색하며 빈칸이면 채움.
# 마지막 슬롯이 차있으면 첫 번째로 돌아가 밑으로 다시 탐색. key 값들이 연속된 특정 슬롯에 모여 있는 것을 'cluster'라고 함.
# cluster가 많거나 그 사이즈가 크면 부정적. 탐색이나 삽입 시 충돌 이후 클러스터를 만나면 클러스터를 따라 계속 탐색해야 해서 수행 시간이 오래 걸리기 때문.
# Quadratic probing(이동폭이 제곱수.)(ex) 충돌이 일어나면 1^2칸 옮김. 거기서 또 충돌 일어나면 최초 충돌 발생한 곳에서 2^2칸 옮김. ...) 초기 해시 값이 같으면 탐사 위치가 같아 효율성 떨어짐.
# Double hashing은 2개의 hash function을 준비하여 하나는 최초 해시 값을 얻기 위해, 다른 하나는 충돌 시 이동폭을 얻기 위해 사용.

self

# Hash Table 구현 by Open Addressing(Linear Probing). resize 가능.
class HashOpenAddressing: # Open Addressing 중 Linear Probnig
    def __init__(self, size = 10, ratio = 1/2):
        self.size = size # slot 개수
        self.items = 0
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.resizeRatio = ratio
    
    def __iter__(self):
        for i in range(self.size)
            yield self.keys[i]

    def __str__(self):
        s = "|"
        for a in self:
            if a == None:
                b = f"{'':<5}|"
            else:
                b = f"{'a':^5}|"
            s += b
        return s
    
    def __len__(self):
        return self.items

    def hashFunction(self, key):
        return key % self.size

    # key 값이 있으면 해당하는 slot 번호 return. 없다면 item이 저장될 slot 번호 return.
    def findSlot(self, key): # key가 들어가게 될 slot 찾기.
        i = self.hashFunction(key)
        start = i
        while self.keys[i] != None and self.keys[i] != key:
            i = (i + 1) % self.size # 이 문장은 마지막의 다음 순서가 첫 번째로 하기 위함. 원형 구조.
            if i == start:
                return None
        return i

    def move(self): # size 늘린 새로운 table로 옮기기.
        oldSize = self.size
        oldKeys = self.keys
        oldValues = self.values
        self.size *= 2
        self.items = 0
        self.keys = [None] * self.size
        self.values = [None] * self.size
        for i in range(oldSize):
            if oldKeys[i] != None:
                self.set(oldKeys[i], oldValues[i])
        del oldKeys
        del oldValues

    def set(self, key, value = None):
        if len(self) > self.size * self.resizeRatio: # item의 수가 슬롯 개수의 반 보다 많으면
            self.move()
            print("resize({self.size//2} -> {self.size})", end =" ")
        i = self.findSlot(key)
        if i == None:
            print("H is full now.")
            return None
        if self.keys[i] != None: # key 값이 이미 있다면
            self.values[i] = value
        else:
            self.keys[i] = key
            self.values[i] = value
            self.items += 1
        return key

    def search(self, key):
        i = self.findSlot(key)
        if i != None and self.keys[i] != None: # key가 들어갈 곳이 있고, key 값이 이미 있다면
            return self.values[i]
        else:
            return None

# H    slot 번호
# A0       0
# A1       1
# B0       2
# A3       3
# B3       4
# C0       5
#          6
# remove는 지운다고 끝나는 게 아니라. 밑에 있는 것을 지운 칸으로 옮길지 말지도 관건이다.
# 예를 들어 빈칸을 메우는 작업 없이 A1을 지우고 search(B0)를 하면 먼저 번호 0을 방문할 것인데, A0가 있어서 1로 내려가게 된다. 그런데 1이 빈칸이기 때문에 테이블에 B0이 없는 것으로 인식하게 된다(B0가 실제로 있음에도).
# 그렇다면 B0를 번호 1로 옮긴다면 번호 2가 비는데, A3를 옮겨야 할까? 아니다. 옮긴다면 search(A3)가 실패할 것이기 때문이다. 대신 번호 5에 있는 C0를 번호 2에 옮겨야 한다.
# A0       0
# B0       1
# C0       2
# A3       3
# B3       4
#          5
#          6
# C0를 옮긴 후 5번 밑인 6번으로 내려간다. 근데 6번이 빈칸이기 때문에 옮기는 작업을 종료한다.
# H[i]는 삭제하여 빈 슬롯이고, 그 아래쪽인 H[j]에 있는 아이템을 빈 슬롯 H[i]로 이동할지 말지 결정한다고 하자.
# H[j].key 값의 hash function 값이 k라고 하면, i < k <= j일 때 H[j]를 H[i]로 옮기면 안 된다.
# 원형 구조이기 때문에 j < i < k 나 k <= j < i 일 때도 안 된다.
# 만약 옮긴다면 H[j].key 값으로 탐색할 때 없다고 나오는 문제 등이 발생할 수 있기 때문이다.
    def remove(self, key):
        i = self.findSlot(key)
        if i == None:
            return None
        if self.keys[i] == None:
            return None
        j = i # H[i]는 지워질 슬롯, H[j]는 옮겨질 슬롯
        while True:
            self.keys[i] = None # H[i] 비우기
            while True:
                j = (j + 1) % self.size
                if self.keys[j] == None:
                    self.items -= 1
                    return key
                




# key 값이 있으면 해당하는 slot 번호 return. 없다면 item이 저장될 slot 번호 return.
def findSlot(key):
    i = f(key) # i는 slot 번호, f는 hash function
    start = i
    while(H[i] == occupied) and (H[i].key != key): # occupied는 i 번째 슬롯이 꽉 차있다는 것. 이미 아이템이 있다는 것.
        i = (i+1) % m # %m 해주는 건 마지막 다음이 첫 번째로 하기 위함.
        if i == start: # 한 바퀴 다 돌았다면
            return FULL # key 값을 슬롯이 없고, 빈 슬롯도 없다면 FULL return.
    return i

# 1. key 값이 H에 있으면 value를 update 2. key 값이 H에 없으면 (key, value)를 실제로 insert.
def set(key, value=None):
    i = findSlot(key)
    if i == FULL: # 저장할 공간이 없는 것 Full(H 용량을 키워야 하는 상태)
        return FULL
    if H[i] is occupied:
        H[i].value = value
        return key
    else:
        H[i].key = key
        H[i].value = value
        return key

# search는 해당하는 key가 있으면 key와 value 값을 돌려줌.
def search(key):
    i = findSlot(key)
    if H[i] is occupied:
        return H[i].value
    else:
        return NOTFOUND

# remove(key): key 값을 찾아 해당하는 아이템이 있으면 슬롯을 빈칸으로 만듦.
# 슬롯 하나를 지우면 빈칸이 생기는데
# 밑에 있는 것들을 빈칸으로 옮겨서 채울지 말지
# 고민하는 것이 문제.

# H[i]는 삭제하여 빈 슬롯이고, 그 아래쪽인 H[j]에 있는 아이템을 빈 슬롯 H[i]로 이동할지 말지 결정한다고 하자.
# H[j].key 값의 hash function 값이 k라고 하면, i < k <= j일 때 H[j]를 H[i]로 옮기면 안 된다.
# 원형 구조이기 때문에 j < i < k 나 k <= j < i 일 때도 안 된다.
# 만약 옮긴다면 H[j].key 값으로 탐색할 때 없다고 나오는 문제 등이 발생할 수 있기 때문이다.
def remove(key):
    i = findSlot(key)
    if H[i] is unoccupied: # 삭제할 아이템이 없다면
        return NOTFOUND
    j = i # H[i]: 비어질 슬롯, H[j]: 옮겨질 슬롯
    while True:
        H[i] = unoccupied # H[i]를 비워 줌.
        while True: # 이사할 H[j]를 찾기
            j = (j+1) % m
            if H[j] is unoccupied: # 이사할 게 없다면
                return key # key를 지우고 해야 할 이동까지 다 마치고 끝남.
            k = f(H[j].key)
            if not (i < k <= j or j < i < k or k <= j < i): # 괄호 안의 조건이 아니라면 이동 가능.
                break 
        H[i] = H[j] # break 후 while문 빠져나가고 나서 옮겨 줌.
        i = j



# clust 길이가 길수록 탐색, 삽입 연산 등의 수행 시간이 많이 듦.
# clust 길이에 영향을 미치는 것은 hash function과 collision resolution method.
# linear probing은 꼭 좋은 방법은 아님. 충돌 발생할 때마다 clust 길이 하나 증가하기에.


## oepn addressing과 대비되는 다른 충돌 회피 방법은 chaining
# open addressing은 한 slot당 들어갈 수 있는 entry가 하나지만 chaining은 아님.
# chaining은 각 slot을 연결리스트로 관리.