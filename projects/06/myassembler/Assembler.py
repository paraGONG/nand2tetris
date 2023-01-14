from Parser import *

filePath = '../rect/Rect.asm'
file = open(filePath, mode='r')
data = file.read().splitlines()
binaryOut1 = parser(data.copy(),True)
pc = -1
binaryOut2 = parser(data)
file.close()
outputPath = '../rect/Rect.hack'
file = open(outputPath, mode='w')
file.write(binaryOut2)
file.close()
