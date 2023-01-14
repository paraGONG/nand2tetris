# 预定义符号
table = {'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4, 'SCREEN': 16384, 'KBD': 24576}
for i in range(0, 16):
    table['R' + str(i)] = i

ramAddress = 16


def addEntry(symbol, address):
    table[symbol] = address


def contains(symbol):
    return symbol in table


def getAddress(symbol):
    return table[symbol]
