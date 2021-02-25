# A function that filters the given text by removing all chars that are not alpha or space
# and replacing '\n' with ' '
# Function takes O(n) time where n is the length of the text
def filterText(text):
	filteredText = ''

	for char in text:
		if char.isalpha() or char == ' ':
			filteredText += char
		elif char == '\n':
			filteredText += ' '

	return filteredText

# A function that returns the list of the words that are in the given text
# Function takes O(n) time where n is the length of the text
def extractWordsFromText(text):
	filteredText = filterText(text)
	wordsList = filteredText.split()
	return wordsList

# A function that returns number of words in the given text
# Function takes O(n) time where n is the length of the text
def getWordCount(text):
	wordsList = extractWordsFromText(text)
	return len(wordsList)

# A function that returns number of letters in the given text
# Function takes O(n) time where n is the length of the text
def getNumberOfLetters(text):
	wordsList = extractWordsFromText(text)
	onlyLettersString = ''.join(wordsList)	# One string that consists of letters
	return len(onlyLettersString)

# A function that returns the longest word in the given text
# Function takes O(n) time where n is the length of the text
def getLongestWord(text):
	wordsList = extractWordsFromText(text)
	maxLength = -1
	maxWord = ''

	for word in wordsList:
		if len(word) > maxLength:
			maxLength = len(word)
			maxWord = word

	return maxWord

def getAverageWordLength(text):
	return getNumberOfLetters(text) / getWordCount(text)

import math

# A function that calculates the reading duration in minutes and seconds
# It is estimated that an avarage person reads 200 to 250 words in a minute
# This parameter can be passed as parameter. Default value is 200
# Function takes O(n) time where n is the length of the text
def getReadingDurationInSeconds(text, WORDS_PER_MINUTE = 200):
	wordCount = getWordCount(text)
	minutes = math.floor(wordCount / WORDS_PER_MINUTE)
	afterDecimal = (round((((wordCount / WORDS_PER_MINUTE) - math.floor(wordCount / WORDS_PER_MINUTE)) * 100)))
	seconds = round(afterDecimal / 100 * 60)

	return str(minutes) + 'm' + str(seconds) + 's'



# A function that returns the median word length
# Function takes O(n) time where n is the length of the text
def getMedianWordLength(text):
	wordsList = extractWordsFromText(text)
	wordCount = len(wordsList)
	mid = math.floor(wordCount / 2)

	# If there are even numbers of words then the median value will be the avarage of the middle two words' lengths
	if wordCount % 2 == 0:
		medianWordLength = (len(wordsList[mid]) + len(wordsList[mid - 1])) / 2
	# If there are odd numbers of words than the median value will be the middle word's length
	else:
		medianWordLength = len(wordsList[mid])

	return medianWordLength

# A function that returns the median word length when the words are sorted by their length
# Function takes O(n) time where n is the length of the text
def getSortedMedianWordLength(text):
	wordsList = extractWordsFromText(text)
	sortedWordsList = sorted(wordsList, key=len)

	wordCount = len(sortedWordsList)
	mid = math.floor(wordCount / 2)

	# If there are even numbers of words than the median value will be the avarage of the middle two words' lengths
	if wordCount % 2 == 0:
		medianWordLength = (len(sortedWordsList[mid]) + len(sortedWordsList[mid - 1])) / 2
	# If there are odd numbers of words than the median value will be the middle word's length
	else:
		medianWordLength = len(sortedWordsList[mid])

	return medianWordLength

def getTopFiveMostCommonWords(text):
	wordsList = extractWordsFromText(text)

	wordsDict = {}
	for word in wordsList:
		if word in wordsDict:
			wordsDict[word] += 1
		else:
			wordsDict[word] = 1

	return wordsDict

# A function that guess the text language for english/turkish based on the stop words
# Function takes O(n) time where n is the length of the text (Stop words stored as sets (hash tables))
def guessTextLanguage(text):
	wordsList = extractWordsFromText(text)

	for word in wordsList:
		if word in stopWordsForEN:
			return 'en'
		elif word in stopWordsForTR:
			return 'tr'

	return ''

# Stop words taken from the https://www.ranks.nl/stopwords
stopWordsForEN = {	'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 
					'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 
					'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", 
					"i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 
					'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 
					'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 
					'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', 
					"why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves'
				 }
stopWordsForTR = {	'acaba', 'altmış', 'altı', 'ama', 'bana', 'bazı', 'belki', 'ben', 'benden', 'beni', 'benim', 'beş', 'bin', 'bir', 'biri', 'birkaç', 'birkez', 'biz', 'bizden', 'bizi', 
					'bizim', 'bu', 'buna', 'bunda', 'bundan', 'bunu', 'bunun', 'da', 'daha', 'dahi', 'de', 'defa', 'diye', 'doksan', 'dokuz', 'dört', 'elli', 'gibi', 'hem', 'hep', 'hepsi', 'her', 'hiç', 'iki',
					'ile', 'mi', 'ise', 'için', 'katrilyon', 'kez', 'ki', 'kim', 'kimden', 'kime', 'kimi', 'kırk', 'milyar', 'milyon', 'mu', 'mi', 'nasıl', 'ne', 'neden', 'nerde', 'nerede', 'nereye', 'niye', 
					'niçin', 'on', 'ona', 'ondan', 'onlar', 'onlardan', 'onları', 'onların', 'onu', 'otuz', 'sanki', 'sekiz', 'seksen', 'sen', 'senden', 'seni', 'senin', 'siz', 'sizden', 'sizi', 'sizin', 
					'trilyon', 'tüm', 've', 'veya', 'ya', 'yani', 'yedi', 'yetmiş', 'yirmi', 'yüz', 'çok', 'çünkü', 'üç', 'şey', 'şeyden', 'şeyi', 'şeyler', 'şu', 'şuna', 'şunda', 'şundan', 'şunu'
				 }

def test(text):
	print('Word count: ' + str(getWordCount(text)))
	print('Number of letters: ' + str(getNumberOfLetters(text)))
	print('The longest word: ' + getLongestWord(text))
	print('Average Word Length: ' + str(getAverageWordLength(text)))
	print('Reading Duration: ' + str(getReadingDurationInSeconds(text)))
	print('Median Word Length: ' + str(getMedianWordLength(text)))
	print('Sorted Median Word Length: ' + str(getSortedMedianWordLength(text)))
	#print(getTopFiveMostCommonWords(text))
	print('Text Language: ' + guessTextLanguage(text))