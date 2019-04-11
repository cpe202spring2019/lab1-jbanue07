
def max_list_iter(int_list):
   if int_list is None:
       raise ValueError
   elif not int_list:
       return None
   max = int_list[0]
   for i in range(len(int_list)):
      if int_list[i] > max:
         max = int_list[i]
   return max


def reverse_rec(int_list):
   if int_list is None:
       raise ValueError
   elif int_list == []:
       return []
   new_list = []
   n = len(int_list)
   if n == 1:
      return int_list
   else:
      new_list.append(int_list.pop(n-1))
      return new_list + reverse_rec(int_list)


def bin_search(target, low, high, int_list):
    if int_list == None:
        raise ValueError
    if high < 0 and low < 0:
        return None
    if high < low:
        return None
    if low > len(int_list) - 1:
        return None
    if low < 0:
        return None
    if high > len(int_list)-1:
        return None
    span = high-low
    if span == 1:
        if target == int_list[low]:
            return low
        elif target == int_list[high]:
            return high
        else:
            return None
    if span == 2:
        if target == int_list[low]:
            return low
        elif target == int_list[high]:
            return high
        elif target == int_list[high-1]:
            return high-1
        else:
            return None
    if span%2 == 0:
        mid = int(span/2 + low)
    elif span%2 == 1:
        mid = int((span-1)/2 + low)
    if target == int_list[mid]:
        return mid
    elif target < int_list[mid]:
        mid = mid - 1
        return bin_search(target, low, mid, int_list)
    elif target > int_list[mid]:
        mid = mid + 1
        return bin_search(target, mid, high, int_list)



