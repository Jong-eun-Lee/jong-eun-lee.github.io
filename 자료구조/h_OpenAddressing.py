### Open Addressing
## Linear Probing
# 작성자: 이종은

### 충돌 회피 방법(Collision Resolution Method)의 대표적 방법은 Open addressing과 Chaining.
## open addressing -> 충돌할 경우 다른 빈칸을 찾아 저장시키는 것. 한 slot당 들어갈 수 있는 entry가 하나.
# open addressing에는 linear probing, qudratic probing, double hashing 등이 있다.

# Linear Probing - 충돌이 일어나면 거기서 밑으로 고정된 이동폭에(선형적) 따라 (예를 들어 한 칸씩) 탐색하며 빈칸이면 채움.
# 마지막 슬롯이 차있으면 첫 번째로 돌아가 밑으로 다시 탐색. key 값들이 연속된 특정 슬롯에 모여 있는 것을 'cluster'라고 함.
# cluster가 많거나 그 사이즈가 크면 부정적. 탐색이나 삽입 시 충돌 이후 클러스터를 만나면 클러스터를 따라 계속 탐색해야 해서 수행 시간이 오래 걸리기 때문.

# Quadratic probing(이동폭이 제곱수.)(ex) 충돌이 일어나면 1^2칸 옮김. 거기서 또 충돌 일어나면 최초 충돌 발생한 곳에서 2^2칸 옮김. ...) 초기 해시 값이 같으면 탐사 위치가 같아 효율성 떨어짐.
# Double hashing은 2개의 hash function을 준비하여 하나는 최초 해시 값을 얻기 위해, 다른 하나는 충돌 시 이동폭을 얻기 위해 사용.

#!!! ※ Hash Table 구현 전이므로 pesudo code 섞여 있음.
# Hash Table 만들 땐 pesudo code 없이 구현.



## Linear Probnig
# key 값이 있으면 slot 번호 return. 없다면 item이 저장될 slot 번호 return.
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

