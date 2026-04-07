list = [3, 3, 3, 3, 3, 3, 3]
S = 21

def find_sum(list, S):
       left = 0
       right = 0
       sum_now = list[0]

       while right < len(list):
              if sum_now == S:
                     if right - left >= 1:
                            return list[left:right + 1]
                     else:
                            right += 1
                            if right < len(list):
                                   sum_now += list[right]
              elif sum_now < S:
                     right += 1
                     if right < len(list):
                            sum_now += list[right]
              else:
                     sum_now -= list[left]
                     left += 1

                     if left > right and left < len(list):
                            right = left
                            sum_now = list[left]

       return None

result = find_sum(list,S)
print(result)