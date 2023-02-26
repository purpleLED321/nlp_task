import spacy
nlp = spacy.load('en_core_web_sm')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("food")
# its the highest similarity combo despite not sharing any letters which is interesting as it shows spacy recognises that they are both animals
print(word1.similarity(word2))

# only shares 'n' yet spacy knows bananas are linked to monkeys as they like to eat them.
print(word3.similarity(word2))

# its interesting because nothing is linked so its low similarity.
print(word3.similarity(word1))

# its interesting that it did not find a very strong similarity, because banana is a type of food, so i would've expected a higher similarity.
print(word3.similarity(word4))

print('\n')

# original number 0.59, 0.40, 0.22, 0.34
# simpler moodel numbers, 0.68, 0.73, 0.68, 0.53
# it thinks cat and monkey are more similar which is interesting because it got it more right despite being a simpler model
# it also thinks banana and monkey are more similar which is interesting because it got it more right despite being a simpler model
'''
# interesting to see the link
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
'''
