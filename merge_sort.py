def merge_sort(my_list):
   if len(my_list) > 1:
      mid = len(my_list)//2
      left_half = my_list[:mid]
      right_half = my_list[mid:]
      merge_sort(left_half)
      merge_sort(right_half)


      i = j = k = 0
      while i < len(left_half) and j < len(right_half):
         if left_half[i] < right_half[j]:
            my_list[k] = left_half[i]
            i += 1
         else:
            my_list[k] = right_half[j]
            j += 1
         k += 1
      while i < len(left_half) : 
         my_list[k] = left_half[i]
         i +=1
         k +=1

      while j < len(right_half):
         my_list[k] = right_half[j]
         j += 1 
         k += 1


# creating an empty list
my_list = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input())
    # adding the element
    my_list.append(ele)  
merge_sort(my_list)
print(my_list)
