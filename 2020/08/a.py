import sys


accumulator = 0


def parse_op(line):
    op, arg = line.strip().split()
    return op, int(arg.replace('+', ''))


def handle_acc(pc, arg):
    global accumulator
    accumulator += arg
    return pc + 1


def handle_nop(pc, arg):
    return pc + 1


def handle_jmp(pc, arg):
    return pc + arg


handlers = {
    'acc': handle_acc,
    'nop': handle_nop,
    'jmp': handle_jmp,
}


def main():
    pc = 0
    visited_lines = set()
    operations = [parse_op(line) for line in sys.stdin.readlines()]
    while True:
        op, arg = operations[pc]
        visited_lines.add(pc)
        pc = handlers[op](pc, arg)
        if pc in visited_lines:
            print(accumulator)
            print('loop')
            break
        if pc >= len(operations):
            print(accumulator)
            print('termination')
            break


if __name__ == '__main__':
    main()
