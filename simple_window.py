list = [1, 2, 3, 4, 5, 6]
S = 9

def find_S(list, S):

       left = 0
       right = 0
       add = list[0]

       while right < len(list):
              if add == S:
                     if right - left >= 1:
                            return list[left:right + 1]
                     else:
                           right += 1 
                           if right < len(list):
                                   add += list[right]

              elif add < S:
                     right += 1
                     if right < len(list):
                            add += list[right]

              else:
                     add -= list[left] 
                     left += 1

                     if left > right and left < len(list):
                            right = left 
                            add = list[left] 

       return None        

result = find_S(list, S)
print(result)