from sentence_splitter import SentenceSplitter
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
with open("text.txt", "r") as f:
    file_text = f.read()

splitter = SentenceSplitter(language='en')
sentences = splitter.split(text=file_text)
sentence_map = {}


def get_sentiment(wordToCheck):
    positive_words = ["good", "great", "excellent", "happy", "well"]
    negative_words = ["bad", "terrible", "poor", "unhappy", "not", "unfortunately"]
    punctuation = [",", "?", "!", ".", ":", ";", "'"]
    if wordToCheck.lower() in positive_words:
        return "1"
    elif wordToCheck.lower() in negative_words:
        return "-1"
    elif wordToCheck.lower() in punctuation:
        return "punctuation"
    else:
        return "0"


for i, sentence in enumerate(sentences):
    words = word_tokenize(sentence)
    word_sentiments = []
    # print("i: ", i)
    # print("sentence: ", sentence)
    # print("words: ", words)
    for word in words:
        sentiment = get_sentiment(word)
        word_sentiments.append((word, sentiment))

    sentence_map[i] = [sentence, word_sentiments]

for key, value in sentence_map.items():
    print("Sentence:", value[0])
    print("Words with sentiment labels:")
    for word, sentiment in value[1]:
        print(f"{word}: {sentiment}")
    print()

print("Bütün map: ")
for key, value in sentence_map.items():
    print(key, ": ", value)
tryingList = []
print(" ")
for key, value in sentence_map.items():
    tryingList.append(value[1])

print(tryingList)
