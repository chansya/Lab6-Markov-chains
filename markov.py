"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents


def make_chains(text_string, n):
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

    for i in range(len(words)-n):
        key = tuple(words[i:i+n])
        if key not in chains:
            chains[key] = [words[i+n]]
        else:
            chains[key].append(words[i+n])

    return chains


def make_text(chains, n):
    """Return text from chains."""

    words = []
    # use choice method to generate a random word-pair as starting words
    while True:
        starting_words = choice(list(chains.keys()))
        if starting_words[0][0].isupper():
            break

    words.extend(starting_words)

    while True:

        try:
            # following word would be a random word from the value list
            following_word = choice(chains[starting_words])

            words.append(following_word)

            starting_words = tuple(words[-n:])

        except KeyError:
            break

    return ' '.join(words)


input_path = 'dr-seuss.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 2)

# Produce random text
random_text = make_text(chains, 2)

print(random_text)
