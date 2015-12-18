
'''                                                                                                                 
Mangle Verbs v1.0
Thu Sep  3 06:53:57 AEST 2015
'''
from CountSyllables import CountSyllables

class MangleVerbs(object):

        def __init__(self):
		self.syllables = CountSyllables()

        def filterVerbs(self):
                fileName = open("verbs.txt", "r")
                data = fileName.read()
                fileName.close()
                data = data.split("\n")

                fileName2 = open("dict.txt", "r")
                commonWords = fileName2.read()
                fileName2.close()
                commonWords = commonWords.split("\n")

                output = open("output.txt", "w")
                                             
                for word in data:
                        word = word.strip().lower()
                        number = self.syllables.count(word)

                        #print word, number
                        
                        if number == -1:
                                number = self.syllables.oldCount(word)

                        if number == 1:
                                if word in commonWords:
                                        print "killed: ", word
                                        continue
                                output.write(word + "\n")
                                print "added: ", word

                                

                
                output.close()

def main():
	test = MangleVerbs()
	test.filterVerbs()

if __name__ == '__main__':main()
