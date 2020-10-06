from parsing import remove_comments, is_l, is_c, is_a
""" Functions for assembling Hack Machine Language Code into Binary"""


class SymbolTable:
    def __init__(self):
        self.symbols = {'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4,
                        'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3,
                        'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7,
                        'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11,
                        'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15,
                        'SCREEN': 16384, 'KBD': 24576}

    def append(self, key, value):
        self.symbols[key] = value

    def lookup(self, key):
        if key in self.symbols:
            return str(
                self.symbols.get(key)
            )
        else:
            return None

    def store_labels(self, assembly_code):
        source = open(assembly_code)
        rom_address = 0
        for line in source:
            line = remove_comments(line)
            if line.endswith("\n"):
                line = line[:-1]
            if not line:
                continue
            line = str.strip(line)
            if is_l(line):
                self.symbols[line[1:-1]] = rom_address
            elif is_a(line) or is_c(line):
                rom_address += 1
