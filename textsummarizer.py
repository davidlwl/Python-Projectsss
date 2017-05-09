
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def summarize(input_file, output_num):
    #take out specific stop words
    stop_words = set(stopwords.words('english'))
    #split input text into sentences
    with open(r'C:\Users\Davidlwl\Desktop\Python Projects\input_file.txt', 'r') as f:
        input_text = f.read().replace("\n", "")
        input_text = ''.join(input_text)
        input_text = sent_tokenize(input_text)
        #getting freq of each word into a dict  
    word_values = {}
    for sentence in input_text:
        words = sentence.split(' ')
        for word in words:
            word = strip(word)
            if not word in stop_words:
                if not word in word_values:
                    word_values[word] = 1
                else:
                    word_values[word] += 1

    sentence_values = []
    for sentence in input_text:
        sentence_value = 0   
        words = sentence.split(' ')
        for word in words:
        #counts the sentence value using word_values dictionary

            
            sentence_value += word_values.setdefault(word, 0)
        sentence_values.append(sentence_value)
        

    #how many sentences do you want = output_num
    for ii in range(0, output_num):
        highest_val_ind = sentence_values.index(max(sentence_values))
        print(input_text[highest_val_ind])
        print('-' * 80)              
        del input_text[highest_val_ind]
        del sentence_values[highest_val_ind]

def strip(word):
    return word.strip().strip(',').strip(':').strip('(').strip(')').lower()

if __name__ == "__main__":
    summarize("input_file.txt", 5)

