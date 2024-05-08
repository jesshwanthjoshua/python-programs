def addition (num1, num2):
  return num1+num2

def subtraction (num1, num2):
  return num1-num2

def multiplication (num1, num2):
  return num1*num2

def division (num1, num2):
  return num1/num2

def modulo_division(num1, num2):
  return num1%num2

calculator_dictionary = {
  "+" : addition, 
  "-" : subtraction, 
  "*" : multiplication, 
  "/" : division, 
  "%" : modulo_division
}

def calculator():
  num1 = float(input("What's the first number : "))
  continue_operation = True
  while continue_operation:
    symbol = input("Declare the operation you need to perform '+', '-', '*', '/', '%' : ")
    operation = calculator_dictionary[symbol]
    num2 = float(input("What's the next number : "))
    answer = operation(num1, num2)
    print(f"{num1} {symbol} {num2} = {answer}")
    
    con_cal = input("To continue the calculation type 'y', or to start new calculation type 'new', or to close the calculator type 'n': ")
  
    if con_cal == "n":
      continue_operation = False
    elif con_cal == "new":
      continue_operation = False
      calculator()  
    else:
      num1 = answer

calculator()