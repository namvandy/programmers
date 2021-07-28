def insertion_sort():
    #삽입 정렬
    #왼쪽부터 오른쪽까지 점점 커지는 순서로 정렬된 배열
    left_num = num_list[0]
    for i in range(len(num_list)):
        if i==0:
            pass
        elif num_list[i]<num_list[i-1]:
            num_list[i]=num_list[i-1]
            num_list[i-1] = num_list[i]
        elif num_list[i]>num_list[i-1]:
            pass
        
    return num_list

def selection_sort():

    return []

def bubble_sort():

    return []

n = int(input())
num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

insertion_sorted_list = insertion_sort()
print(" ".join(map(str, insertion_sorted_list)))

selection_sorted_list = selection_sort()
print(" ".join(map(str, selection_sorted_list)))

bubble_sorted_list = bubble_sort()
print(" ".join(map(str, bubble_sorted_list)))
