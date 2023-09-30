def bil_prima() :
  List = []
  a = 100
  for num in range(a): 
      if num > 1: 
          for i in range(2,num): 
              if (num % i == 0): 
                  break
          else :
              List.append(num)
  return List

def primeX(x):
    y = bil_prima()
    return y[x-1]

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29