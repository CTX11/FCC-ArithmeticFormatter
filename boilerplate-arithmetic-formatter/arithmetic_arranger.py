import re


def arithmetic_arranger(problems, solve = False):
    # this
    # ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]

    # into this
   # "    3      3801      45      123\n+ 855    -    2    + 43    +       49\n-----    ------    ----    -----"  


   if(len(problems) > 5):
     return "Error: Too many problems."


   first = ""
   second = ""
   dashes = ""
   solutionx = ""
   string = ""
   for problem in problems:
     if(re.search("[^\s0-9.+-]", problem)):
       if(re.search("[/]", problem) or re.search("[*]", problem)):
        return "Error: Operator must be '+' or '-'."
       return "Error: Numbers must only contain digits."

     firstNumber = problem.split(" ")[0]
     operator = problem.split(" ")[1]
     secondNumber = problem.split(" ")[2]

     if(len(firstNumber) >= 5 or len(secondNumber) >= 5):
       return "Error: Numbers cannot be more than four digits."

     sum = ""
     if(operator == "+"):
      sum = str(int(firstNumber) + int(secondNumber))
     elif(operator == "-"):
      sum = str(int(firstNumber) - int(secondNumber))

     length = max(len(firstNumber), len(secondNumber)) + 2
     top = str(firstNumber).rjust(length)
     bottom = operator + str(secondNumber).rjust(length - 1)
     dash = ""
     res = str(sum).rjust(length)
     for s in range(length):
        dash += "-"

     if problem != problems[-1]:
       first += top + '    '
       second += bottom + '    '
       dashes += dash + '    '
       solutionx += res + '    '
     else:
       first += top
       second += bottom
       dashes += dash
       solutionx += res


   if solve:
      string = first + "\n" + second + "\n" + dashes + "\n" + solutionx
   else:
      string = first + "\n" + second + "\n" + dashes
   return string



  