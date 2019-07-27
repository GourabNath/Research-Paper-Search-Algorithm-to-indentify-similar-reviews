#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk


# In[ ]:


#De-Emojify
def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')


# In[ ]:


#Remove Special Symbols other than (.), (,) and (!)
def removeSymbols(inputString):
    return(inputString.translate(str.maketrans("", "", "#$%&\'()*+-/:;<=>?@[\\]^_`{|}~")))


# In[ ]:


#Remove (.), (,) and (!) for later stage
def remove_dot_comma_excl(inputString):
    s = inputString.translate(str.maketrans(".", " ", ""))
    s = s.translate(str.maketrans(",", " ", ""))
    s = s.translate(str.maketrans("!", " ", ""))
    return(' '.join(s.split()))


# In[ ]:


#Text cleaning function -> Return a list of tokenized sentence
#(Which will be used for word tokenizarion followed by POS tagging)

def clean_review(review):
    r = review.lower()
    r = removeSymbols(r)
    r = deEmojify(r)
    r = nltk.sent_tokenize(r)

    tokens = []
    for sentence in r:
        s = remove_dot_comma_excl(sentence)
        if len(s) > 0:
            tokens.append(s)
    return(tokens)

