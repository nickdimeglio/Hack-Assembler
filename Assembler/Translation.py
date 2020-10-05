from Parsing import *

""" Functions for translating a list of 
    already-parsed Hack Machine Language commands 
    into a list of 16-bit binary commands"""


def translate_a(cmd):
    binary = "0" + bin(cmd['Address'])
    return binary


def translate_c(cmd):
    return cmd
