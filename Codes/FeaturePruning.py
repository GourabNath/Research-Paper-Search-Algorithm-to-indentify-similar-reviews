#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from nltk.tokenize import sent_tokenize


# In[ ]:


#NEW - Number of commonly used conjunctions present between the two words]

conjunctions = ['however', 'and', 'that', 'but', 'or', 'as', 'if', 'when', 'than',
               'because', 'while', 'where', 'after', 'so', 'though', 'since', 'until', 'whether', 
               'before', 'although', 'nor', 'like', 'once', 'unless', 'except']

def nconjunctions(a,b,sentence):
    count = 0
    words = sentence.split()

    if (a in sentence) and (b in sentence):
        pos1 = min(words.index(a), words.index(b))
        pos2 = max(words.index(a), words.index(b))

        for word in words[pos1:pos2+1]:
            if word in conjunctions:
                count +=1

    return(count)


# In[ ]:


#Compactness Pruning
def compact4(a,b, reviews):
    count = 0
    compact = []
    nconj = 0
    nsentence = 0
    
    for review in reviews:                                                        
        sentences = sent_tokenize(review)
        s =[]
        for sentence in sentences:
            nsentence += 1
            if sentence[len(sentence)-1] == '.':
                sentence = sentence.rstrip('.')
            if (f1 in sentence) & (f2 in sentence):
                count += 1
                rev_list = sentence.split()     
                comp = abs(rev_list.index(f1) - rev_list.index(f2))-1
                s.append(comp)
                if comp <= 3:
                    #count the number of conjunctions:
                    nconj += nconjunctions(a,b,sentence)
                    
            else:
                s.append(-1)
        compact.append(s)
    
    compact_arr = []
    for lst in compact:
        for elements in lst:
            compact_arr.append(elements)
        
    compact_arr = np.array(compact_arr)
    score = sum((compact_arr <= 3) & (compact_arr > 0))
    
    output = {'compact': compact, 'n_sentence': count,  'm':score, 'nconjunc': nconj,
             'nsentence': nsentence}

    return(output)
    


# In[ ]:


#Redundancy Pruning
def redundancy(f, F, reviews):
    k = 0
    m = 0
    for review in reviews:
        sentences = sent_tokenize(review)

        for sentence in sentences:
            if sentence[len(sentence)-1] == '.':
                        sentence = sentence.rstrip('.')

            if f in sentence:
                m += 1

                for feature in F:
                    w = feature.split()
                    if (w[0] in sentence) and (w[1] in sentence):
                        words = sentence.split()
                        compact = abs(words.index(w[0]) - words.index(w[1]))
                        if compact < 3:
                            k += 1

    p_supp = m - k
    return(p_supp)

