""" Functions for parsing Hack Machine Language Code.
    'Parse' produces the list of parsed commands"""


def remove_comments(string):
    comment = string.find("//")
    if comment != -1:
        return string[:comment]
    return string


# For checking command types
def is_l(cmd):
    return cmd.__contains__('(')


def is_c(cmd):
    return cmd.__contains__('=') or cmd.__contains__(';')


def is_a(cmd):
    return cmd[0] == '@'


def has_variable(address):
    return not str.isdigit(str(address))


# For parsing commands of known types
def parse_c(cmd):
    dest_bound = cmd.find('=')
    if dest_bound == -1:
        dest_bound = 0
        dest = None
    else:
        dest = cmd[:dest_bound]

    jump_bound = cmd.find(';')
    if jump_bound == -1:
        jump = None
    else:
        jump = cmd[jump_bound + 1:]

    if dest and jump:
        comp = cmd[dest_bound + 1:jump_bound - 1]
    elif dest:
        comp = cmd[dest_bound + 1:]
    elif jump:
        comp = cmd[:jump_bound]

    parsed = {"Type": "Computation",
              "Comp": comp,
              "Dest": dest,
              "Jump": jump,
              }
    return parsed


def parse_a(cmd):
    parsed = {"Type": "Address",
              "Address": cmd[1:],
              }
    return parsed


def parse(assembly_code, symbol_table):
    source = open(assembly_code)
    ram_address = 16
    commands = []

    for line in source:

        # Prep text
        line = remove_comments(line)
        if line.endswith('\n'):
            line = line[:-1]
        if not line:
            continue
        command = str.strip(line)

        # Parse and store A commands
        if is_a(command):
            if has_variable(command[1:]):
                if not symbol_table.lookup(command[1:]):
                    symbol_table.append(command[1:], ram_address)
                    ram_address += 1
                command = "@" + symbol_table.lookup(command[1:])
            commands.append(
                parse_a(command)
            )

        # Parse and Store C commands
        elif is_c(command):
            commands.append(
                parse_c(command)
            )

        if is_l(command):
            continue
    return commands
