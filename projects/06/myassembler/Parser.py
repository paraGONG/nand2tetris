from SymbolTable import *
from Code import *
import re

pc = -1


def parser(instructions, isFirst=False):
    return advance(instructions, isFirst)


def hasMoreCommands(instructions):
    return True if len(instructions) > 0 else False


def advance(instructions, isFirst):
    global pc, ramAddress
    binaryOut = ''
    while hasMoreCommands(instructions):
        current = instructions.pop(0).strip()
        if (isInstructionInvalid(current)):
            continue
        current = re.sub(r'//.*', '', current).strip()
        type = commandType(current)
        if type == 'C':
            if not isFirst:
                d = dest(current)
                c = comp(current)
                j = jump(current)
                binaryOut += '111' + c + d + j + '\n'
            else:
                pc += 1
        elif type == 'A':
            if not isFirst:
                token = symbol(current, type)
                binary = ''
                if token.isdigit():
                    binary += int2Binary(token)
                else:
                    if contains(token):
                        binary = int2Binary(getAddress(token))
                    else:
                        binary = int2Binary(ramAddress)
                        addEntry(token, ramAddress)
                        ramAddress += 1
                binaryOut += binary + '\n'
            else:
                pc += 1
        elif type == 'L':
            if (isFirst):
                token = symbol(current, type)
                addEntry(token, pc + 1)
    return binaryOut


def symbol(instruction, type):
    if type == 'A':
        return instruction[1:]
    elif type == 'L':
        return instruction[1:-1].strip()


def int2Binary(num):
    b = str(bin(int(num)))[2:]
    while len(b) != 16:
        b = '0' + b
    return b


def commandType(insturction):
    if insturction[0] == '@':
        return 'A'
    elif insturction[0] == '(':
        return 'L'
    else:
        return 'C'


def isInstructionInvalid(instruction):
    if instruction == '' or re.match(r'^//', instruction):
        return True
    return False
