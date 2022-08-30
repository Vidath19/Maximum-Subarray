def max_crossing_subArray(A, low, mid, high):

   sum = 0
   left_sum = float('-inf')
   max_left = mid

   for i in range(mid, low-1, -1):
        sum = sum + A[i]
        if (sum > left_sum):
            left_sum = sum
            max_left=i

   sum = 0
   right_sum = float('-inf')
   max_right = mid+1
   for i in range(mid + 1, high + 1):
      sum = sum + A[i]
      if (sum > right_sum):
         right_sum = sum
         max_right =i+1

   return max_left,max_right,left_sum+right_sum

def max_sub_array(A, low, high):

    if high == low:
      return (low,high,A[low])
    else:
        mid=(low+high)//2
        left_low,left_high,left_sum=max_sub_array(A,low,mid)
        right_low, right_high, right_sum = max_sub_array(A,mid+1,high)
        cross_low,cross_high,cross_sum = max_crossing_subArray(A,low,mid,high)
        if left_sum >= right_sum and left_sum>=cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum>= left_sum and right_sum>=cross_sum:
            return (right_low, right_high,right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


my_list = [7,4,3,8,2,9]
list_length = len(my_list)
print("The list is :")
print(my_list)

max = max_sub_array(my_list, 0, list_length-1)
print("The maximum value is ")
print(max)