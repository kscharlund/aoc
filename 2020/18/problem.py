import sys
from pprint import pprint
import math


def parse(line, left_in=None):
    token, line = line[0], line[1:]
    if token == '(':
        left, line = parse(line)
    else:
        assert token.isdigit()
        left = (int(token),)

    if left_in:
        left = left_in + (left,)

    if not line:
        return left, line
    token, line = line[0], line[1:]
    if token == ')':
        return left, line

    assert token in {'+', '*'}
    res, line = parse(line, (token, left))
    return res, line


def evaluate(expr):
    if len(expr) == 1:
        return expr[0]
    op, left, right = expr
    if op == '+':
        return evaluate(left) + evaluate(right)
    else:
        assert op == '*'
        return evaluate(left) * evaluate(right)


precedence_a = {
    '+': 1,
    '*': 1,
}


precedence_b = {
    '+': 2,
    '*': 1,
}


def dijkstra_parse(line, precedence):
    op_stack = []
    out_queue = []
    for token in line:
        if token.isdigit():
            out_queue.append(int(token))
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            while op_stack and op_stack[-1] != '(':
                out_queue.append(op_stack.pop())
            op_stack.pop()
        else:
            while op_stack and op_stack[-1] != '(' \
                    and precedence[token] <= precedence[op_stack[-1]]:
                # Note: equal precedence should only pop stack if
                # token is a left associative operator.
                out_queue.append(op_stack.pop())
            op_stack.append(token)
        # print(token, out_queue, op_stack)
    while op_stack:
        out_queue.append(op_stack.pop())
    return out_queue


def eval_rpn(tokens):
    # print(tokens)
    stack = []
    for token in tokens:
        if token == '+':
            res = stack.pop() + stack.pop()
        elif token == '*':
            res = stack.pop() * stack.pop()
        else:
            res = token
        stack.append(res)
    assert len(stack) == 1
    return stack[0]


def a(lines):
    print(sum(evaluate(parse(line)[0]) for line in lines))
    print(sum(eval_rpn(dijkstra_parse(line, precedence_a)) for line in lines))


def b(lines):
    print(sum(eval_rpn(dijkstra_parse(line, precedence_b)) for line in lines))


def main():
    lines = [line.strip().replace(' ', '') for line in sys.stdin.readlines()]
    a(lines)
    print()
    b(lines)


if __name__ == '__main__':
    main()
