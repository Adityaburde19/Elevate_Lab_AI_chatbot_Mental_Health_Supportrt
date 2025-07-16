from nltk.corpus import stopwords
import re
import nltk

nltk.download('stopwords')

offensive_words = {'suicide', 'kill', 'murder', 'die', 'depressed'}

def is_offensive(text):
    words = set(re.findall(r'\w+', text.lower()))
    return not offensive_words.isdisjoint(words)
