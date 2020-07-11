


# Importando as bibliotecas necessárias
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
import sys

# Criando a função
def calculate_frequencies(file_name):
    # Aqui está uma lista de palavras desinteressantes para a nuvem de palavras:
    fhand = open(file_name)
    texto = fhand.read()
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
   
    words = dict()
    result = re.sub('[!-.:-@]',"", texto)
    result = result.split()
    
    for word in result:
        if word in result:
            word.lower()
        if word not in uninteresting_words:
            words[word] = words.get(word, 0) + 1
        
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(words)
    return cloud.to_array()


# Gerando a imagem:

myimage = calculate_frequencies("poema.txt")
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()


