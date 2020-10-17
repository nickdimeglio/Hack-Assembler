from parsing import is_label_cmd, is_computation_cmd, is_address_cmd
""" Functions for assembling Hack Machine Language Code into Binary"""


class SymbolTable:
    def __init__(self):
        self.symbols = {'SP': "0", 'LCL': "1", 'ARG': "2", 'THIS': "3", 'THAT': "4",
                        'R0': "0", 'R1': "1", 'R2': "2", 'R3': "3",
                        'R4': "4", 'R5': "5", 'R6': "6", 'R7': "7",
                        'R8': "8", 'R9': "9", 'R10': "10", 'R11': "11",
                        'R12': "12", 'R13': "13", 'R14': "14", 'R15': "15",
                        'SCREEN': "16384", 'KBD': "24576"}

    def lookup(self, key):
        return self.symbols.get(key, None)

    def store_labels(self, assembly_code):
        source = open(assembly_code)
        rom_address = 0
        for line in source:
            line = line.strip()
            if (not line) or line.startswith('//'):  # skip if empty or is comment
                continue
            if is_label_cmd(line):
                self.symbols[line[1:-1]] = str(rom_address)
            elif is_address_cmd(line) or is_computation_cmd(line):
                rom_address += 1
