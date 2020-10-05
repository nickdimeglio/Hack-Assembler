from SymbolTable import *
from Parsing import *
from Translation import *
"""Main file for assembling Hack Assembly Code into binary"""

source = "Max2.asm"

# Create a new symbol table, store labels from source code
symbol_table = SymbolTable()
symbol_table.store_labels(source)

# Parse source code file into a list of commands
commands = parse(source, symbol_table)

for command in commands:
    print(command)
# Translate parsed commands into a list of binary commands
# binary = []
# for command in commands:
#     if command['type'] == "Address":
#         bin_cmd = translate_a(command)
#     elif command['type'] == "Computation":
#         bin_cmd = translate_c(command)
#     binary.append(bin_cmd)
#
# # Write list of binary commands to a .hack file
# source_name = source[:str.find(source, ".asm")]
# binary_file = open(source_name + ".hack", 'wb')
#
# for instruction in binary:
#     binary_file.write(instruction + '\n')


