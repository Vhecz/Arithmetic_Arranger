def arithmetic_arranger(problems, answer_problems=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  arranged_problems = ""
  top_row = ""
  bottom_row = ""
  dashes = ""
  answer_row = ""

  for problems in problems:
    operands = problems.split()
    operand1 = operands[0]
    operator = operands[1]
    operand2 = operands[2]

    if operator not in ('+', '-'):
      return "Error: Operator must be '+' or '-'."
      
    if not operand1 .isdigit() or not operand2 .isdigit():
      return "Error: Numbers must only contain digits."
      
    if len(operand1) > 4 or len(operand2) > 4:
      return "Error: Numbers cannot be more than four digits."

    space_width = max(len(operand1), len(operand2)) + 2

    top_row += operand1.rjust(space_width) + "    "
    bottom_row += operator + operand2.rjust(space_width - 1) + "    "
    dashes += "-" * (space_width) + "    "

    if answer_problems:
      if operator == '+':
        answer = str(int(operand1) + int(operand2))
      else:
        answer = str(int(operand1) - int(operand2))
      answer_row += answer.rjust(space_width) + "    "

  arranged_problems += (
    top_row.rstrip() + "\n" + bottom_row.rstrip() + "\n" + dashes.rstrip())
    
  if answer_problems:
        arranged_problems += "\n" + answer_row.rstrip()

  return arranged_problems