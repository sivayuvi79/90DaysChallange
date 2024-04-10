num = int(input("Enter a number you want to add"))
result = 0
for i in range(1, num + 1):
  result = result + i
  print(result)
print(result)


def Solution2(num, test=1):
  return (num * (num + 1)) / 2
