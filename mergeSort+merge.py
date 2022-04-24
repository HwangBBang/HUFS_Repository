def merge_sort(array):              #병합 정렬
    if (len(array)<=1):
        return array
    else:
        mid = len(array)//2         # 반나누기
        left = merge_sort(array[0:mid])
        right = merge_sort(array[mid:len(array)])
    return merge(left, right)
def merge(S1, S2):                  # S라는 빈 리스트 에 append 시키는 방법을 이용한 merge함수다.
    S = []
    i = j = 0
    while(i<len(S1) and j<len(S2)) :
        if S1[i]<S2[j]:             # 각 리스트의 크기를 비교 하여 작은것을 append 한다.
            S.append(S1[i])
            i+=1
        else:                       # 각 리스트의 크기를 비교 하여 작은것을 append 한다.
            S.append(S2[j])
            j+=1
    if i < len(S1):       
        S += S1[i: len(S1)]
    else:
        S += S2[j: len(S2)]
    return S
    
    
    #################################################################################
    
def merge(S1,S2,S):                 
    i = j = 0
    while i+j<len(S):
        if j ==len(S2) or (i<len(S1)and S1[i]<S2[j]):
            S[i+j] = S1[i]
            i+=1
        else:
            S[i+j] = S2[j]
            j+=1
def merge_sort(S):
    n = len(S)
    if n < 2:
        return
    mid = n//2
    S1 = S[0:mid]
    S2 = S[mid:n]
    merge_sort(S1)
    merge_sort(S2)
    
    merge(S1,S2,S)
    #202103769 황병훈
