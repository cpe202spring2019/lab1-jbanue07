
def max_list_iter(int_list):
   max = 0
   if int_list is None:
       raise ValueError
   elif int_list == []:
       return None
   for i in range(len(int_list)):
      if int_list[i] > max:
         max = int_list[i]
   return max


def reverse_rec(int_list):
   if int_list is None:
       raise ValueError
   new_list = []
   n = len(int_list)
   if int_list == []:
       return None
   if n == 1:
      return int_list
   else:
      new_list.append(int_list.pop(n-1))
      return new_list + reverse_rec(int_list)


def bin_search(target, low, high, int_list):
    span = high-low
    if span == 1:
        if target == int_list[low]:
            return low
        elif target == int_list[high]:
            return high
        else:
            return None
    elif int_list == None:
        raise ValueError
    if span%2 == 0:
        mid = int(span/2 + low)
    elif span%2 == 1:
        mid = int((span-1)/2 + low)
    if target == int_list[mid]:
        return mid
    elif target < int_list[mid]:
        mid = mid -1
        return bin_search(target, low, mid, int_list)
    elif target > int_list[mid]:
        mid = mid + 1
        return bin_search(target, mid, high, int_list)



