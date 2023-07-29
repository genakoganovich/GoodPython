import re
expression = list(map(lambda x: str(x).strip(), re.split(r'(\s*[+-]\s*)', input())))
operands = [int(expression[i]) for i in range(len(expression)) if not i % 2]
operators = [expression[i] for i in range(len(expression)) if i % 2]

result = operands[0]
operands = operands[1:]
for i in range(len(operands)):
    if operators[i] == '+':
        result += operands[i]
    else:
        result -= operands[i]
print(result)
