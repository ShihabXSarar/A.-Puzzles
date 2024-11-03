def cann_rearrange(s):
  sort1=sorted(s)
  sort2=reversed(sort1)
  if s==sort1:
      if(s==sort2):
          return False,s
      else:
          return True,sort2
  else :
      return True,sort1

def main():
  t = int(input())
  for _ in range(t):
    s = input()
    can_rearrange, rearranged_string = cann_rearrange(s)
    if(len(s)<=1):
        print("NO")
    elif can_rearrange:
      print("YES")
      print(*rearranged_string)
    else:
      print("NO")

if __name__ == "__main__":
  main()
