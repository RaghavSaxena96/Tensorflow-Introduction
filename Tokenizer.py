import tensorflow as tf 
from tensorflow.keras.preprocessing.text import Tokenizer

sentences=['I am Raghav','I love Cats','I love Gym','I hate Dogs','I hate Milk']

token=Tokenizer(num_words=100)

token.fit_on_texts(sentences)
print(token.word_index)