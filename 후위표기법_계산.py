math_expression = input("연산자 피연산자 한번에 정확하게 띄어쓰기 해주세요!! ex) ( 1 + 23 ) + 45 ")
op_stack = []
stack = []
tokens = math_expression.split()

def top(list):
    return list[-1]

for i in tokens:
    if i == '+' or i == "-" or i == '*' or i == "/" :
        if len(op_stack) == 0:
            op_stack.append(i)
        else:
            if top(op_stack) == '*' or top(op_stack) == '/':
                if i == '*' or i == '/' or i == '+' or i == "-":
                    stack.append(top(op_stack))
                    op_stack.pop()
                    op_stack.append(i)
                    if len(op_stack) > 1:
                        if op_stack[-2] == '+' or op_stack[-2] == '-':
                            stack.append(op_stack[-2])
                            op_stack.pop(-2)
            elif top(op_stack) == '+' or top(op_stack) == '-':
                if i == '+' or i == "-":
                    stack.append(top(op_stack))
                    op_stack.pop()
                    op_stack.append(i)
                elif i == '*' or i == "/":
                    op_stack.append(i)
            elif top(op_stack) == '(':
                op_stack.append(i)

    elif i == '(':
        op_stack.append(i)

    elif i == ")":
        while top(op_stack) != '(':
            stack.append(top(op_stack))
            op_stack.pop()
        op_stack.pop()
    else:
        stack.append(i)
while len(op_stack) != 0:
    stack.append(top(op_stack))
    op_stack.pop()

print(math_expression, " 을 후위표기법 변환시", "".join(stack)," 입니다.")
print(stack)

def calculator(stack):
    cal = []
    for k in stack:
        if k == '+':
            cal.append(cal.pop() + cal.pop())
        elif k == '-':
            cal.append(cal.pop() - cal.pop())
        elif k == '*':
            cal.append(cal.pop() * cal.pop())
        elif k == '/':
            t = cal.pop()
            cal.append(cal.pop() / t)
        else:
            cal.append(int(k))
    return cal.pop()

print("계산 결과 ", calculator(stack), " 입니다.")






