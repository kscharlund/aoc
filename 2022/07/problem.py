from collections import defaultdict
import enum
import sys
from pprint import pprint
import math


def memoize(func):
    """
    Memoization decorator for a function taking a single argument.
    """

    class Memodict(dict):
        """Memoization dictionary."""

        def __missing__(self, key):
            ret = self[key] = func(key)
            return ret

    return Memodict().__getitem__


class State(enum.Enum):
    WANT_COMMAND = enum.auto()
    WANT_FILE = enum.auto()


def handle_line(line, state, fp, fs, cwd: list[str]):
    match state:
        case State.WANT_COMMAND:
            assert line.startswith("$")
            cmd = line.split()[1:]
            if cmd == ["ls"]:
                return fp.readline(), State.WANT_FILE
            elif cmd[0] == "cd":
                if cmd[1] == "/":
                    cwd.clear()
                elif cmd[1] == "..":
                    cwd.pop()
                else:
                    # TODO: check that dir exists?
                    cwd.append(cmd[1])
                print(cmd, cwd)
                return fp.readline(), State.WANT_COMMAND
            else:
                assert False, "unexpected command"
        case State.WANT_FILE:
            if line.startswith("$"):
                return line, State.WANT_COMMAND
            size, name = line.split()
            if size != "dir":
                path = "/" + "/".join(cwd + [name])
                fs[path] = int(size)
            return fp.readline(), State.WANT_FILE
    return line, state


def get_data():
    filesystem = {}
    cwd = []
    with open(sys.argv[1]) as fp:
        line, state = fp.readline(), State.WANT_COMMAND
        while line:
            line, state = handle_line(line, state, fp, filesystem, cwd)
        pprint(filesystem)
    return filesystem


def a(data):
    sums = defaultdict(int)
    for path in sorted(data):
        dirs = path.split("/")[:-1]
        for i in range(0, len(dirs)):
            sums["/".join(dirs[: i + 1])] += data[path]
        # sums["/"] += data[path]
    pprint(sums)
    print(sum(d for d in sums.values() if d <= 100000))


def b(data):
    sums = defaultdict(int)
    for path in sorted(data):
        dirs = path.split("/")[:-1]
        for i in range(0, len(dirs)):
            sums["/".join(dirs[: i + 1])] += data[path]
        # sums["/"] += data[path]
    free = 70000000 - sums[""]
    req = 30000000 - free
    print(req)
    for key, val in sorted(sums.items(), key=lambda x: x[1]):
        if val > req:
            print(key, val)


def main():
    data = get_data()
    a(data)
    print()
    b(data)


if __name__ == "__main__":
    main()
