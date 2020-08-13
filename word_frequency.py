STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

# Function to clean up an 
def clean_function():
            for char in line.lower():
                if char.isalpha():
                    filteredwords.append(char)
                elif char.isspace():
                    word = "".join(filteredwords)
                    filteredwords = []
                    



def print_word_freq(file):
    wordfreq = {}
    with open(file) as infile:
        for line in infile:
            wordlist = []
            for char in line.lower():
                if char.isalpha():
                    wordlist.append(char)
                elif char.isspace():
                    word = "".join(wordlist)
                    wordlist = []
                    if word not in STOP_WORDS:
                        if word in wordfreq:
                            wordfreq[word] += 1
                        else: wordfreq[word] = 1

    width = max([len(k) for k in wordfreq])
    for k in wordfreq:
        print(f"{k} | {wordfreq[k]} {'=)' * wordfreq[k]}")

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
