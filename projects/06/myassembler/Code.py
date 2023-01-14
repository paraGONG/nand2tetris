# jump域集合
jSet = {
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111',
}

# comp域集合
cSet = {
    '0': '0101010',
    '1': '0111111',
    '-1': '0111010',
    'D': '0001100',
    'A': '0110000',
    'M': '1110000',
    '!D': '0001101',
    '!A': '0110001',
    '!M': '1110001',
    '-D': '0001111',
    '-A': '0110011',
    '-M': '1110011',
    'D+1': '0011111',
    'A+1': '0110111',
    'M+1': '1110111',
    'D-1': '0001110',
    'A-1': '0110010',
    'M-1': '1110010',
    'D+A': '0000010',
    'D+M': '1000010',
    'D-A': '0010011',
    'D-M': '1010011',
    'A-D': '0000111',
    'M-D': '1000111',
    'D&A': '0000000',
    'D&M': '1000000',
    'D|A': '0010101',
    'D|M': '1010101',
}


# 解析dest域
def dest(instruction):
    if '=' in instruction:
        d = instruction.split('=')[0].strip()
        temp = ['0','0','0']
        for char in d:
            if char == 'A':
                temp[0] = '1'
            elif char == 'D':
                temp[1] = '1'
            elif char == 'M':
                temp[2] = '1'
        return ''.join(temp)
    return '000'


# 解析comp域
def comp(instruction):
    c = instruction
    if '=' in c:
        c = c.split('=')[1].strip()
    if ';' in c:
        c = c.split(';')[0].strip()
    c = c.replace(' ','')
    if c in cSet:
        return cSet[c]
    else:
        if '+' in c or '|' in c or '&' in c:
            c = c[::-1]
            if c in cSet:
                return cSet[c]
    return 'error'


# 解析jump域
def jump(instruction):
    if ';' in instruction:
        j = instruction.split(';')[1].strip()
        return jSet[j]
    return '000'