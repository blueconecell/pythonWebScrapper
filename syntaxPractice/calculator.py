def inputFirstNum():
  print("Choose a number:")
  num = int(input())
  return num


def inputSecondNum():
  print("Choose another one:")
  num = int(input())
  return num


def inputOperation():
  print('''Choose an operation:
    Options are: +, -, *, /.
    Write 'exit' to finish.''')
  oper = input()
  return oper
  
##########
## main ##
##########
while True:
  firstNum = inputFirstNum()
  secondNum = inputSecondNum()
  oper = inputOperation()

  if oper == "exit":
    break
  elif oper == "+":
    print("Result:", firstNum + secondNum)
  elif oper == "-":
    print("Result:", firstNum - secondNum)
  elif oper == "*":
    print("Result:", firstNum * secondNum)
  elif oper == "/":
    print("Result:", firstNum / secondNum)
