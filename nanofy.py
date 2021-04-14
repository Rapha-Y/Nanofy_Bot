import random

#separate text into a list of sentences and punctuations
def separate_text(txt):
    separators = [",", ".", "!", "?"]

    sentence_list = []
    punctuation_list = []

    #0 for sentence, 1 for punctuation
    current_list = 0
    item_to_add = ""

    for i in range(len(txt)):
        #current character is a separator
        if txt[i] in separators:
            #last character was not a separator
            if current_list == 0:
                sentence_list.append(item_to_add)
                item_to_add = txt[i]
                current_list = 1
            #last character was a separator
            else:
                item_to_add = item_to_add + txt[i]
        #current character is not a separator
        else:
            #last character was not a separator
            if current_list == 0:
                item_to_add = item_to_add + txt[i]
            #last character was a separatoxr
            else:
                punctuation_list.append(item_to_add)
                item_to_add = txt[i]
                current_list = 0

    if current_list == 0:
        sentence_list.append(item_to_add)
    else:
        punctuation_list.append(item_to_add)

    return (sentence_list, punctuation_list)

#randomly add nanora to all sentences of the text
def nanofy(txt):
    #split the text into sentences and punctuation
    sentence_list, punctuation_list = separate_text(txt)

    #always add nanora to the last sentence
    last_index = len(sentence_list) - 1
    sentence_list[last_index] = sentence_list[last_index] + " nanora" 

    #add nanora to the other sentences at 30% chance
    for i in range(len(sentence_list) - 1):
        if random.random() < 0.3:
            sentence_list[i] = sentence_list[i] + " nanora"

    #match lists size
    if len(sentence_list) > len(punctuation_list):
        punctuation_list.append("")

    #merge sentences and punctuation
    nano_txt_list = []
    zip_txt = zip(sentence_list, punctuation_list)
    for pair in zip_txt:
        for val in pair:
            nano_txt_list.append(val)
    nano_txt = ("").join(nano_txt_list)

    return nano_txt