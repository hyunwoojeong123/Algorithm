def selection_sort(my_list,start,end):
    if start >= end:
        return
    else:
        #print(some_list)
        for j in range(start, end):
            if my_list[j] < my_list[start]:
                k = my_list[j]
                my_list[j] = my_list[start]
                my_list[start] = k
            else:
                pass
        selection_sort(my_list,start+1,end)


some_list = [11, 3, 6, 4, 12, 1, 2]
selection_sort(some_list,0,len(some_list))
print(some_list)