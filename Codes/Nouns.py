#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk


# In[ ]:


#Function to get nouns from the text 
#Input: Clean review (Output of the function clean_review)
#Output: Nouns (present in the review)

def get_nouns(clean):
    nouns = []
    for sentence in clean:
        pos = nltk.pos_tag(nltk.word_tokenize(sentence))
        for (a,b) in pos:
            if (b == 'NN' or b == 'NNS') and len(a) > 2:
                nouns.append(a)
    return(set(nouns))

