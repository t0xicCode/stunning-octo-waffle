#!/usr/bin/env python3

import sys
import re
from collections import deque


given_re = re.compile(r'^When I (?P<op>add|multiply|subtract|divide) (?P<one>.*?) to (?P<two>.*?)$')
then_re = re.compile(r'^Then I expect the value (?P<sol>.*)$')


def parse_scenario(lst):
# lst will always have at least one line
    _, name = lst.popleft().split(' ', maxsplit=1)
    print('Executing scenario:', name)

# parse constants here

    while len(lst) > 1:
        grst = given_re.match(lst.popleft())
        trst = then_re.match(lst.popleft())
        if grst is None or trst is None:
            print('Error, aborting scenario')
            return

        # run the stuff.
        print('-> When I', grst.group('op'), grst.group('one'), 'to', grst.group('two'))
        print('-> Then I expect the value', trst.group('sol'), end=' ')
        if grst.group('op') == 'add':
# run the stuff
            pass


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('You need to give me a string :)')
        sys.exit(1)

# get all lines from the scenario
    with open(sys.argv[1]) as f:
        lines = deque(f.readlines())

    if len(lines) < 1:
        print('Seems like the scenario file was empty?')
        sys.exit(2)

    while True:
        if len(lines) == 0:
            break
        l = lines.popleft().strip()

# We skip all empty lines
        while l == '':
            if len(lines) == 0:
                break
            l = lines.popleft().strip()

# we ran out of lines and they are all empty
        if len(lines) == 0 and l == '':
            break

        scenario = deque()
        scenario.append(l)

# we have more lines
        if len(lines) > 0:
            continuation = lines.popleft().strip()

            while continuation != '' and not continuation.lower().startswith('scenario'):
                scenario.append(continuation)
                if len(lines) == 0:
                    break
                continuation = lines.popleft().strip()

        parse_scenario(scenario)
