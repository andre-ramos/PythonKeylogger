directoryRead = 'test.txt'
directoryWrite = 'codifiqued.txt'

fileRead = open(directoryRead,'r')
fileWrite = open(directoryWrite,'w')

letter = fileRead.readline()


for line in fileRead:
	if(line.rstrip('\n') != '1111111'):
		word = line.rstrip('\n')
		
		if(word=='1000000'): fileWrite.write('a') 
		elif(word=='0100100'): fileWrite.write('b') 
		elif(word=='0011001'): fileWrite.write('c')
		elif(word=='0001111'): fileWrite.write('d')
		elif(word=='0100001'): fileWrite.write('e')
		elif(word=='0010000'): fileWrite.write('f')
		elif(word=='0100101'): fileWrite.write('g')
		elif(word=='0000010'): fileWrite.write('h')
		elif(word=='0011000'): fileWrite.write('i')
		elif(word=='0100111'): fileWrite.write('j')
		elif(word=='0010001'): fileWrite.write('k')
		elif(word=='0101000'): fileWrite.write('l')
		elif(word=='0000111'): fileWrite.write('m')
		elif(word=='0100110'): fileWrite.write('n')
		elif(word=='0010010'): fileWrite.write('o')
		elif(word=='0100010'): fileWrite.write('p')
		elif(word=='0001000'): fileWrite.write('q')
		elif(word=='0001001'): fileWrite.write('r')
		elif(word=='0011011'): fileWrite.write('s')
		elif(word=='0011010'): fileWrite.write('t')
		elif(word=='0011100'): fileWrite.write('u')
		elif(word=='0000001'): fileWrite.write('v')
		elif(word=='0000000'): fileWrite.write('w')
		elif(word=='0100011'): fileWrite.write('x')
		elif(word=='0100000'): fileWrite.write('y')
		elif(word=='0000101'): fileWrite.write('z')
	
		elif(word=='0011111'): fileWrite.write('0') 
		elif(word=='0101010'): fileWrite.write('1')
		elif(word=='0000100'): fileWrite.write('2')
		elif(word=='0010100'): fileWrite.write('<2/baix>')
		elif(word=='0101011'): fileWrite.write('3')
		elif(word=='0010111'): fileWrite.write('4')
		elif(word=='0101100'): fileWrite.write('<4/esq>')
		elif(word=='0110111'): fileWrite.write('5')
		elif(word=='0000011'): fileWrite.write('6')
		elif(word=='0110000'): fileWrite.write('<6/dir>')
		elif(word=='0110110'): fileWrite.write('7')
		elif(word=='0010011'): fileWrite.write('8')
		elif(word=='0011101'): fileWrite.write('<8/cim>')
		elif(word=='0110101'): fileWrite.write('9')
	
		elif(word=='0000110'): fileWrite.write('<del>')
	
		elif(word=='0111011'): fileWrite.write('\'')
		elif(word=='0111101'): fileWrite.write('-')
		elif(word=='0001110'): fileWrite.write('=')
		elif(word=='0111100'): fileWrite.write('<backs>')
		elif(word=='0111110'): fileWrite.write('/')
		elif(word=='0110100'): fileWrite.write('*')
	
		elif(word=='0111010'): fileWrite.write('<tab>')
		elif(word=='0001101'): fileWrite.write('<acento>')
		elif(word=='0111001'): fileWrite.write('[')
		elif(word=='0101110'): fileWrite.write('<enter>')
		elif(word=='0101111'): fileWrite.write('+')
	
		elif(word=='0001100'): fileWrite.write('<caps>')
		elif(word=='0111000'): fileWrite.write('<cedilha>')
		elif(word=='0011110'): fileWrite.write('<til>')
		elif(word=='0110011'): fileWrite.write(']')
		elif(word=='0110010'): fileWrite.write('.')
	
		elif(word=='0111111'): fileWrite.write('<shift>')
		elif(word=='0010101'): fileWrite.write('\\')
		elif(word=='0010110'): fileWrite.write('<virgula>')
		elif(word=='0110001'): fileWrite.write('<ponto>')
		elif(word=='0001010'): fileWrite.write(';')
	
		elif(word=='0001011'): fileWrite.write(' ')
		elif(word=='0101101'): fileWrite.write('<AltGr>')
		elif(word=='0101001'): fileWrite.write(',')
		
	else:
		fileWrite.write('\n\n')
	
fileRead.close()
fileWrite.close()