""" Functions for parsing Hack Machine Language Code.
    'Parse' produces the list of parsed commands"""


# Functions for checking command types
def is_label_cmd(command):
    """Returns True if the given command is a label command
        such as (termination_loop)"""
    return command.__contains__('(')


def is_computation_cmd(command):
    """Returns True if the given command is a computation command
        such as 'D=2+2;JMP'"""
    return command.__contains__('=') or command.__contains__(';')


def is_address_cmd(command):
    """Returns True if the given command is an address command
        such as '@R1'"""
    return command[0] == '@'


def has_variable(address_command):
    """Returns True if the address of the address command
        contains anything other than digits"""
    return not str.isdigit(str(address_command))


# Functions for parsing commands of known types
def parse_computation(command):
    """Parses a computation command into 3 fields:
    Dest, Comp, and Jump"""
    dest_bound = command.find('=')
    if dest_bound == -1:
        dest_bound = 0
        dest = None
    else:
        dest = command[:dest_bound]

    jump_bound = command.find(';')
    if jump_bound == -1:
        jump = None
    else:
        jump = command[jump_bound + 1:]

    if dest and jump:
        comp = command[dest_bound + 1:jump_bound - 1]
    elif dest:
        comp = command[dest_bound + 1:]
    elif jump:
        comp = command[:jump_bound]

    parsed = {"Type": "Computation",
              "Comp": comp,
              "Dest": dest,
              "Jump": jump,
              }
    return parsed


def parse_address(command):
    """Parses an address command to get just it's address"""
    parsed = {"Type": "Address",
              "Address": command[1:],
              }
    return parsed


def parse(assembly_code, symbol_table):
    """Produces a list of commands by parsing each line of assembly
     into a dictionary that contains it's fields"""
    source = open(assembly_code)
    ram_address = 16
    commands = []

    for line in source:

        # Skip empty lines, comments, and label declarations
        line = line.strip()
        if (not line) or line.startswith('//') or is_label_cmd(line):
            continue

        # Parse and store A commands
        if is_address_cmd(line):
            address = line[1:]
            if has_variable(address):
                if not symbol_table.lookup(address):
                    symbol_table.symbols[address] = str(ram_address)
                    ram_address += 1
                line = "@" + symbol_table.lookup(address)
            commands.append(
                parse_address(line)
            )

        # Parse and Store C commands
        elif is_computation_cmd(line):
            commands.append(
                parse_computation(line)
            )

    return commands
