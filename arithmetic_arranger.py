# Code written by Chooi Fei Ng

def arithmetic_arranger(problems,sol=False):
  # Initialise lists to store the numbers and operators
  temp_sol = []
  temp_op = []
  # Initialise the error flag
  error_flag = 0

  if (len(problems) > 5):
    # The number problems passed into the function are more five, return error message
    arranged_problems = 'Error: Too many problems'
    error_flag = 1
  else:
    # Loop through each of the arithmetic problems passed into the function
    for i in range(len(problems)):
      #print(problems[i])
      if("+" in problems[i]):
        # For + ,split the problem and place the numbers in temp_sol and the operator in temp_op
        temp_math = problems[i].split('+')
        #print(temp_math)
        temp_sol.append(temp_math)
        temp_op.append('+')
        #print(temp_sol)
        #print(temp_op)
      elif("-" in problems[i]):
        # For - , split the problem and place the numbers in temp_sol and the operator in temp_op
        temp_math = problems[i].split('-')
        temp_sol.append(temp_math)
        temp_op.append('-')
      else:
        # The operators are not + or -, return error message
        arranged_problems = 'Error: Operator must be \'+\' or \'-\' '
        error_flag = 1

      #if(range(len(temp_math)) > 4):
  # Initialise the lines to be returned from the function
  line = ''
  line2 = ''
  line3 = ''
  line4 = ''
  #temp_op[0]

  for j in range(len(temp_op)):
    # The numbers passed into the function must only contain digits, otherwise display an error message
    try:
      temp = int(temp_sol[j][0])
      temp2 = int(temp_sol[j][1])
    except:
      arranged_problems = 'Error: Numbers must only contain digits'
      error_flag = 1

    # Loop through each problem based on the number of operators stored
    if (error_flag == 0):
      if (len(temp_sol[j][0].strip()) > 4 or len(temp_sol[j][1].strip()) > 4):
        # Display error if the numbers for each of the problems is more than four digits, and strip the whitespaces when comparing the strings
        arranged_problems = 'Error: Numbers cannot be more than four digits'
        error_flag = 1
        # print(j)
        # print(temp_sol[j][0])
        # print(len(temp_sol[j][0]))
        # print(len(temp_sol[j][1]))
      else:
        if (len(temp_sol[j][1]) > len(temp_sol[j][0])):
        # if the second number is greater than the first number
          # Determine the amount of space needed before each number
          space1 = ' ' * (len(temp_sol[j][1]) - len(temp_sol[j][0])+2) # Space for line 1
          space2 = ' ' # Space for line 2
          # Determine the amount of dashes needed for each problem in line 3
          dashes = '-' * (len(temp_sol[j][1].strip()) +2)

        else:
        # if the first number is greater than the second number
        # Determine the amount of space needed before each number
          space1 = '  ' # Space for line 1
          space2 = ' '*(len(temp_sol[j][0]) - len(temp_sol[j][1]) + 1) # Space for line 2
          # Determine the amount of dashes needed for each problem in line 3
          dashes = '-' * (len(temp_sol[j][0].strip()) + 2)

        # Calculate the addition or subtraction for each problem
        if (temp_op[j] == '+'):
          # for additions
          solution = int(temp_sol[j][0]) + int(temp_sol[j][1])
        else:
          # for subtractions
          solution = int(temp_sol[j][0]) - int(temp_sol[j][1])

        # The problem and solutions arranged vertically
        line =  line + space1 + temp_sol[j][0].strip() + ' '*4
        line2 = line2 + temp_op[j] + space2 + temp_sol[j][1].strip()+ ' '*4
        line3 = line3 + dashes + ' '*4

        if(len(str(solution).strip()) > len(temp_sol[j][1].strip()) and len(str(solution).strip()) > len(temp_sol[j][0].strip())):
          #print('GT')
          #print(len(str(solution).strip()))
          #print(len(temp_sol[j][1].strip()))
          line4 = line4 + ' ' + str(solution).strip() + ' '*4
        else:
          #print('ST')
          line4 = line4 + ' '*2 + str(solution).strip() + ' ' * 4

  # Return the output arranged vertically if there is no errors
  if (error_flag == 0):
    if (sol == True):
      # Include the solution
      arranged_problems = line + '\n' + line2 + '\n' + line3 + '\n' + line4
    else:
      # Does not include the solution
      arranged_problems = line + '\n' + line2 + '\n' + line3

  return arranged_problems