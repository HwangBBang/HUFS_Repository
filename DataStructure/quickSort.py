array = [5,7,9,0,3,1,6,2,4,8]
# 202103769 황병훈
#: 기준데이터 (Pivot)을 설정 한후 좌측에선 큰값 우측에선 작은값을 찾는다.
#각 데이터값을 찾은후 그둘을 교환하고 이과정을 반복한다. 
#위 과정을 반복하다 좌우측 데이터 방향이 엇갈리는경우 작은값과 피벗값의 위치를 서로변경한다.
#피벗값의 위치가 변경되면 좌측은 피벗보다 작은 데이터 값이 남게되고 우측은 피벗보다 큰 데이터 값이 남게된다.
# (Divide) 이제 피벗 기준 좌우측으로 묶인 데이터 뭉치들도 위와같은 과정을 반복하여 (오름차순) 정렬하는 알고리즘이다.
# (큰 데이터 찾기) left --->    <--- right(작은 데이터찾기)

def quickSort1(array, start, end):      ### 첫 번째 방법 ###
    if start >= end:         # 원소가 1개인 경우 종료
        return
    piovt = start            # 피벗은 첫번째 원소
    left = start + 1        # 피벗보다 큰거찾기 left
    right = end             # 피벗보다 작은 데어터찾기 right
    while (left <= right):      #엇갈릴 때 까지 반복
        while(left <= end and array[left]<=array[piovt]): # 피벗보다 큰거 찾을떄까지 한칸씩 이동
            left += 1
        while(start < right and array[right]>= array[piovt]):   # 피벗보다 작은거 찾을 때 까지 이동
            right -=1
        if(left > right):           #큰거찾는 좌측 인덱스와 작은거 찾는 우측인덱스가 엇갈림
            array[right], array[piovt] = array[piovt], array[right]     #엇갈렸다면 피벗값과 우측이 찾은 작은값을 교환
        else:
            array[right], array[left] = array[left], array[right]     #엇갈리지않았다면  좌측이찾은 큰값과 우측이 찾은 작은값을 교환
    quickSort1(array,start,right-1)
    quickSort1(array,left+1,end)
    
def quickSort2(array):        ### 두 번째 방법 ###
    if len(array)<=1:
        return array
    pivot = array[0] #피벗은 첫번째 원소
    tail = array[1:] #피벗을 제외한 리스트는 테일
    left_side = [x for x in tail if x <= pivot] # 피벗보다 작거나같다면 leff
    right_side = [x for x in tail if x > pivot] # 피벗보다 크다면 right
    
    return quickSort2(left_side) + [pivot] + quickSort2(right_side)

def quickSort3(array):      ### 세 번째 방법 ###
    if len(array)<2:
        return
    pivot = array[0]
    L,E,G = [],[],[]        
    while len(array)>0:
        x = array.pop()
        if x<pivot: L.append(x)
        elif x == pivot: E.append(x)
        else: G.append(x)
    quickSort3(L)
    quickSort3(G)
    while len(L)>0:
        array.append(L.pop(0))
    while len(E)>0:
        array.append(E.pop(0))
    while len(G)>0:
        array.append(G.pop(0))
        
print('정렬되기전 리스트',array)
quickSort1(array,0,len(array)-1) # computer는 0부터 세기때문에 -1 을해준다
print('첫번째 솔루션',array)

array = [5,7,9,0,3,1,6,2,4,8]

array=quickSort2(array)
print ('두 번째 솔루션',array)

array = [5,7,9,0,3,1,6,2,4,8]
array = quickSort3(array)
print ('세 번째 솔루션',array)
