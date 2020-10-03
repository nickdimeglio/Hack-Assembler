""" Hack Assembler
    Parser class breaks assembly language command
    into its components, and gives access
    Code class translates each component to binary """

assembly = 0


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def append(self, key, value):
        self.symbols[key] = value

    def lookup(self, key):
        return self.symbols[key]


def first_pass(source, table):
    parsing = source
    rom_a = 0
    for line in parsing:
        if line == pseudo_command:
            table.append()
        elif line == c_instruction:
            rom_a += 1
        elif line == a_instruction:
            rom_a += 1
    return parsing


def second_pass(x, table):
    y = x
    table += 1
    return y


symbol_table = SymbolTable()
stage1 = first_pass(assembly, symbol_table)
stage2 = second_pass(stage1, symbol_table)

c_instruction = 1
a_instruction = 0
pseudo_command = "("








def parse(source_file):
    source = open(source_file, "r")
    commands = {}
    line = 0

    for line in source_file:
        # if line is blank, continue

        # else parse line into fields
        field1, field2, field3 = 0

        #store fields in dictionary, key is line number
        commands[line] = [field1, field2, field3]


def translate(commands):
    for line in commands:
        memory_spot = 16
        # if contains variables, look them up
        #
        # convert each field into proper binary




"""main"""
    # Parser: methods unpack each instruction into fields
    # Code: methods translate each field into binary
    # SymbolTable: methods manage the symbol table
    # Main: initializes the I/O files  (HackAssembler?)
    #       and drives the process


# Reading and parsing commands
    # Start reading a file with a given name
        # Constructor for a Parser object that 
        # accepts a string
        # Specifying a file name
        # Need to know how to read text files
    # Move to the next command in the file
        # Are we finished? boolean hasMoreCommands();
        # Get the next command. void advance();
        # Need to read one line at a time
        # Need to skip whitespace including comments
    # Get the fields of the current command
        # Type of current command (A, C, or Label Defition)
        # Easy access to fields. Assignment will
        # Need Destination, Computation, Jump parts
        # A label or A command "@sum"
        # Access to the actual string
        # String dest(); String comp(); 
        # String Jump(); String label();

# Converting mnemonics -> code
    # Translator?
    # Translate with tables


# Handling Symbols
    # Symbol Table Operations
        # Create a new empty table
        # Add a (symbol, address) pair to the table
        # Does the table contain a given symbol?
        # What is the address associated with a given symbol?
    # Using the symbol table
        # Create a new empty table
        # Add all pre-defined symbols
        # While reading input, add labels and new variables

        # Labels: when you see "(xxx)", add "xxx" and the
        # address of the next machine language command

        # Whenever you see @xxx, where xxx is not a number,
        # consult the table to replace the symbol xxx
        # with its address 
        # If not in table, add "xxx" and the next free
        # address for variable allocation


# Overall Logic
    # Initialization
        # Of Parser
        # Of Symbol Table
    # First Pass
        # Read all commands, only paying attention to
        # labels and updating the symbol table
    # Restart reading and translating commands
    # Main Loop:
        # Get the next Assembly command and parse it
        # For A commands- translate to binary address
        # For C commands- get code for each part 
        #                 and put them together
        # Output the resulting machine language command


