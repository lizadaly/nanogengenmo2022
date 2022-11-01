import random
# list of possible words

words = ["apple", "banana", "cat", "dog", "elephant", "fish", "giraffe", "horse", "iguana", "jaguar", "kangaroo", "lion", "monkey", "narwhal", "octopus", "penguin", "quail", "rhinoceros", "seagull", "toucan", "unicorn", "vulture", "walrus", "xenomorph", "yak", "zebra"]# variables to keep track of word count and sentence count
word_count = 0
sentence_count = 0

# open a new file to write the novel to
f = open("novel.txt", "w")

# write a new sentence to the file until we reach the desired word count
while word_count < 50000:

    # pick a random word from the list
    word = random.choice(words)



    # write the word to the file
    f.write(word + " ")



    # increment the word count
    word_count += 1

    # every 10 words, start a new sentence
    if word_count % 10 == 0:

        f.write("\n")

        sentence_count += 1


    # every 100 sentences, start a new paragraph
    if sentence_count == 100:
        f.write("\n\n")
        sentence_count = 0

# close the file
f.close()