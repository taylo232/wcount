#!/usr/bin/env python3
import sys
import string
import time

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	red='\033[0;31m'
	blue='\033[0;34m'
	white='\033[1;37m'
	green='\033[0;32m'
	lgrey='\033[0;37m'
	yellow='\033[1;33m'
	lblue='\033[1;34m'

def printline():
	print(bcolors.blue + ('-' * 60) + bcolors.yellow)

def countsyllables(word):
	vowel='aeiouy'
	dip=['aa','ae','ai','ao','au','ay','ea','ee','ei','eo','eu','ey','ia','ie','ii','io','iu','iy','oa','oe','oi','oo','ou','oy','ua','ue','ui','uo','uu','uy','ya','ye','yi','yo','yu','yy']
	trip=['aaa','aae','aai','aao','aau','aay','aea','aee','aei','aeo','aeu','aey','aia','aie','aii','aio','aiu','aiy','aoa','aoe','aoi','aoo','aou','aoy','aua','aue','aui','auo','auu','auy','aya','aye','ayu','ayy','eaa','eae','eai','eao','eau','eay','eea','eee','eei','eeo','eeu','eey','eia','eie','eii','eio','eiu','eiy','eoa','eoe','eoi','eoo','eou','eoy','eua','eue','eui','euo','euu','euy','eya','eye','eyu','eyy','iaa','iae','iai','iao','iau','iay','iea','iee','iei','ieo','ieu','iey','iia','iie','iii','iio','iiu','iiy','ioa','ioe','ioi','ioo','iou','ioy','iua','iue','iui','iuo','iuu','iuy','iya','iye','iyi','iyo','iyu','iyy','oaa','oae','oai','oao','oau','oay','oea','oee','oei','oeo','oeu','oey','oia','oie','oii','oio','oiu','oiy','ooa','ooe','ooi','ooo','oou','ooy','oua','oue','oui','ouo','ouu','ouy','oye','oyy','uaa','uae','uai','uao','uau','uay','uea','uee','uei','ueo','ueu','uey','uia','uie','uii','uio','uiu','uiy','uoa','uoe','uoi','uoo','uou','uoy','uua','uue','uui','uuo','uuu','uuy','uye','uyi','uyu','uyy','yaa','yae','yai','yao','yau','yay','yee','yei','yeu','yey','yie','yii','yio','yiu','yiy','yoa','yoe','yoi','yoo','you','yoy','yua','yue','yui','yuo','yuu','yuy','yya','yye','yyi','yyo','yyu','yyy']
	ends2=['ey','oy','ie']
	ends1=['e']
	count=0
	if len(word) <=3:
		count = 1
	else:
		for x in vowel:
				count = count + word.count(x)
		for x in dip:
			count = count - word.count(x)
		for x in trip:
			count = count - word.count(x)
		for x in ends2:
			if word[-2:] == x:
				count = count -1
		for x in ends1:
			if word[-1:] == x:
				count = count -1
	return(count)


total_word=0
total_char=0
total_sentence=0
total_syllable=0
terms=['. ','.\n','?','!',':']
ignore=['\"','(',')','-','_',',',';','\n','\'','.','?','!','*']

### Open File: Look for sys.argv and ask if not present ##

if len(sys.argv) == 1:
	while True:
		myfile = input("Enter filename (*.txt): ")

		if len(myfile) != 0:
			if len(myfile) > 4:
				if (myfile[len(myfile)-4:len(myfile)]) != ".txt":
					myfile = myfile + ".txt"
					break
				else:
					myfile = myfile + ".txt"
					break
else:
	myfile=sys.argv[1]

### try and open file ##
try:
    f=open(myfile,'r')
    word=f.read()
    if len(word) == 0:
        print('File is empty')
        sys.exit()
except:
        print('Unable to open file')
        sys.exit()
mystart = time.time()
print('')
printline()
print("** Analysing",myfile," **")


### Count terminations ###
for x in terms:
	total_sentence = total_sentence + word.count(x)

### Strip out all non-chars and " ". Count characters (discard) ###
for x in ignore:
	foo = word.replace(x, "")
foo=word.replace(" ","")
total_char=len(foo)

### Strip out non-chars and split into word list ###
for x in ignore:
	word = word.replace(x, " ")
word=word.split()
total_word=len(word)

### count syllables ##
word = [element.lower() for element in word]
for x in word:
	total_syllable = total_syllable + countsyllables(x)

### Calculate and print output ###
fleisch=int(206.835 - 1.015*(total_word / total_sentence) - 84.6*(total_syllable/total_word))
ukread=int(0.39*(total_word/total_sentence) + 11.8*(total_syllable/total_word) - 15.59)
printline()
print('UK Reading Grade:\t',ukread + 1)
print('Fleisch Reading Ease:\t',fleisch)
printline()
print('Average word length:\t',"{0:.2f}".format(total_char / total_word))
print('Words per sentence:\t',"{0:.2f}".format(total_word / total_sentence))
print('Sylllables per word:\t',"{0:.2f}".format(total_syllable / total_word))
printline()
#print("Characters: \t\t",total_char)
print("Words: \t\t\t",total_word)
print("Sentences: \t\t",total_sentence)
#print("Sylllables: \t\t",total_syllable)
printline()

myend = time.time()
print('Time taken:\t\t',"{0:.2f}".format(myend - mystart), 'seconds.')
printline()
print('')
