#! /usr/bin/env python


DNASeq = 'ATGTCTCATTCAAAGCA'
DNASeq = raw_input("Enter a DNA sequence: ")
DNASeq = DNASeq.upper()
DNASeq = DNASeq.replace(" ","")
print 'Sequence:', DNASeq

SeqLength = float(len(DNASeq))
print 'Sequence Length:', SeqLength

NumberA = DNASeq.count('A')
NumberC = DNASeq.count('C')
NumberG = DNASeq.count('G')
NumberT = DNASeq.count('T')

print 'A: %.1f%%' % (100 * NumberA /SeqLength)
print 'C: %.1f%%' % (100 * NumberC /SeqLength)
print 'G: %.1f%%' % (100 * NumberG /SeqLength)
print 'T: %.1f%%' % (100 * NumberT /SeqLength)


TotalStrong = NumberG + NumberC
# These are the strongly binding nucleotide pairs
TotalWeak = NumberA + NumberT
# These are the weak binding nucleotide pairs

if SeqLength >= 14:
	# This is a formula that comes out as true if the sequence is 14 or more nucleotides long
	# If the outcome is true, the program continues with the lines in this block
	# If the outcome is false, the program continues with the lines after this block
	MeltTempLong = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength
	# This is a variable to which the formula for the melting temperature when a sequence has more than 14 nucleotide is assigned to
	print "Tm Long (>14): %.1f C" % (MeltTempLong)
	# Prints the literal text: Tm Long (>14): ... C, where the dots are filled with the varible MeltTempLong
else:
	# This is a part of the loop created with 'it' earlier
	# This part of the loop will only happen when the outcome of the formula at line 29 is false
	MeltTemp = (4 * TotalStrong) + (2 * TotalWeak)
	# This is a variable that represents the melting temperature of a nucleotide sequence based on the bindings of the pairs
	print "Melting Temp: %.1f C" % (MeltTemp)
	# I tell the program to print the text 'Melting Temp: C' on the display. 
	# Before the C I tell him to put the variable MeltTemp with one decimal







