import sys
from pprint import pprint


def parse_op(line):
    op, arg = line.strip().split()
    return op, int(arg.replace('+', ''))


next_pc = {
    'acc': lambda pc, arg: pc + 1,
    'nop': lambda pc, arg: pc + 1,
    'jmp': lambda pc, arg: pc + arg,
}

alt_next_pc = {
    'acc': lambda pc, arg: pc + 1,
    'jmp': lambda pc, arg: pc + 1,
    'nop': lambda pc, arg: pc + arg,
}


def find_terminals(parents, child):
    if child not in parents:
        return {child}
    terminals = set()
    for parent in parents[child]:
        terminals |= find_terminals(parents, parent)
    return terminals


def main():
    input_operations = [parse_op(line) for line in sys.stdin.readlines()]
    for altered_index in range(len(input_operations)):
        if input_operations[altered_index][0] == 'acc':
            continue
        operations = input_operations[:]
        old_op, old_arg = input_operations[altered_index]
        operations[altered_index] = ('jmp' if old_op == 'nop' else 'nop', old_arg)
        next_pcs = [next_pc[op[0]](pc, op[1]) for pc, op in enumerate(operations)]
        parents = {}
        for parent, child in enumerate(next_pcs):
            parents.setdefault(child, []).append(parent)
        terminals = find_terminals(parents, len(operations))
        if 0 in terminals:
            print(altered_index, old_op, old_arg)
            break


if __name__ == '__main__':
    main()
