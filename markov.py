"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text_string = open(file_path).read()
    return text_string

#print(open_and_read_file('green-eggs.txt'))
green_eggs_test = open_and_read_file('green-eggs.txt')

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    
    chains = {}
    words = text_string.split()
    words.append(None)
    for i in range(len(words)-2):
        keys = (words[i], words[i +1])       
        values = words[i + 2]
        
        if keys not in chains:
            chains[keys] = []
    
        chains[keys].append(values)
    return chains

green_chains = make_chains(green_eggs_test)


    #need to add word pairs into dictionary
    #make a dictionary
    #loop over words accessing word at i i+1 and i+2
    #modify the loop so youre putting words a i and i+1 in a tuple, use tuple as dict key
    #create a list to store value
    #where do you make the list? check if key is in dictionary if not append
    

    # return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    #links = [[key1,key2,random value],[link2],]

    
    random_key = choice(list(chains.keys()))
    words = [random_key[0], random_key[1]]
    next_word = choice(chains[random_key])
    
    #link = random_key + next_word
    # words = random_key
    
    while next_word is not None:
        next_key = (random_key[1], next_word)
        words.append(next_word)
    #new_key = random_key[1] + ' ' + next_word
    #new_keys_word = choice(chains[new_key])
    # words.append(new_key)
   
    # print(words)
    #words[1]
    # print(words)
 
   # print(random_key)

   # return ' '.join(words)
# make_text(green_chains)
print(make_text(green_chains))

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

#print(random_text)
