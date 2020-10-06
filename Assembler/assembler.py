from symbol_table import *
from translation import *
from parsing import *
import sys
"""Main file for assembling Hack Assembly Code into binary"""

source = sys.argv[1]
# source = "Pong.asm"

# Create a new symbol table, store labels from source code
symbol_table = SymbolTable()
symbol_table.store_labels(source)

# Parse source code file into a list of commands
commands = parse(source, symbol_table)

# Translate parsed commands into a list of binary commands
binary = []
for command in commands:
    if command['Type'] == "Address":
        binary.append(
           translate_a(command))
    elif command['Type'] == "Computation":
        binary.append(
            translate_c(command))

# Write list of binary commands to a .hack file
source_name = source[:str.find(source, ".asm")]
binary_file = open(source_name + ".hack", 'w')

for instruction in binary:
    binary_file.write(instruction + "\n")
