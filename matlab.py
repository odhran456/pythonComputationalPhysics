import wikipedia
from collections import Counter

def clean(string):
    string = string.replace(',', ' ').replace('\n', ' ').replace('.',' ').replace(';',' ')
    return string.lower()


languages = ['c++', 'fortran', 'python', 'java', 'c#','matlab']
page = wikipedia.page('Matlab')
word_counts = Counter(clean(page.content).split(' '))

for language in languages:
    print('{}: {}'.format(language, word_counts[language]))
