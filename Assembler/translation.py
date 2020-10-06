from parsing import *

""" Functions for translating a list of 
    already-parsed Hack Machine Language commands 
    into a list of 16-bit binary commands"""

comp_codes = {"0": "0101010", "1": "0111111", "-1": "0111010",
              "D": "0001100", "A": "0110000", "!D": "0001101",
              "!A": "0110001", "-D": "0001111", "-A": "0110011",
              "D+1": "0011111", "A+1": "0110111", "D-1": "0001110",
              "A-1": "0110010", "D+A": "0000010", "D-A": "0010011",
              "A-D": "0000111", "D&A": "0000000", "D|A": "0010101",
              "M": "1110000", "!M": "1110001", "-M": "1110011",
              "M+1": "1110111", "M-1": "1110010", "D+M": "1000010",
              "D-M": "1010011", "M-D": "1000111", "D&M": "1000000",
              "D|M": "1010101",}
dest_codes = {"null": "000", "M": "001", "D": "010", "MD": "011", "A": "100",
              "AM": "101", "AD": "110", "AMD": "111",}
jump_codes = {"null": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
              "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111",}


def translate_a(cmd):
    binary = format((int(cmd['Address'])), 'b')
    extra_digits = 16 - len(binary)
    binary = "0" * extra_digits + binary
    return binary


def translate_c(cmd):
    comp_bits = comp_codes.get(cmd["Comp"])

    if cmd["Dest"] in dest_codes:
        dest_bits = dest_codes.get(cmd["Dest"])
    else:
        dest_bits = dest_codes.get("null")

    if cmd["Jump"] in jump_codes:
        jump_bits = jump_codes.get(cmd['Jump'])
    else:
        jump_bits = jump_codes.get("null")

    binary = "111" + comp_bits + dest_bits + jump_bits
    return binary



