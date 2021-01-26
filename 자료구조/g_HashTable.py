


### 충돌 회피 방법(collision resolution method)의 대표적 방법은 Open addressing과 Chaining.

## open addressing -> 충돌할 경우 다른 빈칸을 찾아 저장시키는 것. 한 slot당 들어갈 수 있는 entry가 하나.
# open addressing에는 linear probing, qudratic probing, double hashing 등이 있다.
# linear probing - 충돌이 일어나면 거기서 밑으로 고정된 이동폭에(선형적) 따라 (예를 들어 한 칸씩) 탐색하며 빈칸이면 채움. 마지막 슬롯이 차있으면 첫 번째로 돌아가 밑으로 다시 탐색. key 값들이 연속된 특정 슬롯에 모여 있는 것을 'cluster'라고 함. cluster가 많거나 그 사이즈가 크면 안 됨. 클러스터 만나는 경우 계속 밑으로 내려가는데 시간이 오래 걸리게 되니까.



# key 값이 있으면 slot 번호 return. 없다면 item이 저장될 slot 번호 return.
def findSlot(key):
    i = f(key) # i는 slot 번호, f는 hash function
    start = i
    while(H[i] == occupied) and (H[i].key != key): # occupied는 i 번째 슬롯이 꽉 차있다는 것. 누가 있다는 것 이미.
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
    else:
        H[i].key, H[i].value = key, value
    return key

# search는 해당하는 key가 있으면 key와 value 값을 돌려줌.
def search(key):
    i = findSlot(key)
    if H[i] is occupied:
        return H[i].value
    else:
        return NOTFOUND

# remove(key) key 값을 찾아 해당하는 아이템이 있으면 슬롯을 빈칸으로 만듦.
# 슬롯 하나를 지우면 빈칸이 생기는데
# 밑에 있는 것들을 빈칸으로 옮겨서 채울지 말지
# 고민하는 것이 문제다.
# A2와 C2 사이에 빈칸이 있으면
# C2가 없는 것으로 판단 되기 때문에
# C2를 빈칸에 올려줘야 함.
# 빈칸이 있다고 하더라도
# 9자리에 A9가 있는데 올릴 필요는 없음.
# k == f(H[j].key)인 j 자리에 x가 있는데,
# i에 빈칸이 생김. k < i <= j일 때 j에 있는 것을 i에 옮김.
# j < k < i 나 i < j < k 일 때도
def remove(key):
    i = findSlot(key)
    if H[i] is unoccupied:
        return None
    j = i # H[i]: 빈 슬롯, H[j]: 이사해야 할 슬롯
    while True:
        H[i] = None
        while True: # H[j] 찾기
            j = (j+1) % m
            if H[j] is unoccupied:
                return key
            k = f(H[j].key)
            if (k < i <=j): # 다른 두 조건도 있음
                break
        H[i] = H[j]
        i = j
        # 클러스터 길이가 길수록 시간 오래 듦
        # 클러스트의 길이를 결정하는 건 해시 함수
        # 해시 함수가 얼마나 잘 분산시키냐를 결정하기에
        # 분만 아니라 충돌 해결 방법도 영향.
        # linear brobing은 좋은 메소드는 아님
        # 충돌 발생할 때마다 클러스트 길이 하나 증가하기에
# Quadratic probing(이동폭이 제곱수.)(ex) 충돌이 일어나면 1^2칸 옮김. 거기서 또 충돌 일어나면 최초 충돌 발생한 곳에서 2^2칸 옮김. ...) 초기 해시값이 같으면 탐사 위치가 같아 효율성 떨어짐.
# Double hashing은 2개의 hash function을 준비하여 하나는 최초 해시 값을 얻기 위해, 다른 하나는 충돌 시 이동폭을 얻기 위해 사용.

## oepn addressing과 대비되는 다른 충돌 회피 방법은 chaining
# open addressing은 한 slot당 들어갈 수 있는 entry가 하나지만 chaining은 아니다.

