import pickle
import nltk

ct = pickle.load(open('ct.p', 'rb'))
em = pickle.load(open('em.p', 'rb'))
tr = pickle.load(open('tr.p', 'rb'))

'''
for i in ct.keys():
    print i
print len(ct.keys())

'''

import sys

#sent = raw_input('Enter Your Sentence : ')
sent = sys.argv[1]
tokens = nltk.word_tokenize(sent)
print tokens

stokens = []
tags = ct.keys()

for itk, tk in enumerate(tokens):
    if itk==0:
        pstates = ['start']
    else:
        pstates = tags
    scores = {}
    for cstate in tags:#current states
        scores[cstate] = {}
        mx = {}
        mx['score'] = 0.0
        for pstate in pstates:#previous states
            tk = tk.lower() #case insensitive
            try:
                emission = float(em[tk+'_'+cstate])/float(ct[cstate])
            except KeyError:
                emission = 0
            try:
                transmission = float(tr[cstate+'_'+pstate])/float(ct[pstate])
            except KeyError:
                transmission = 0

            if itk>0:
                score = emission * transmission * stokens[itk - 1][pstate]['score']
            else:
                score = emission * transmission

            if score>mx['score']:
                mx['score'] = score
                mx['tag'] = pstate
        scores[cstate] = mx
    #check if no tags matched, give it NNP
    flag = 0
    for key in scores.keys():
        if scores[key]['score']!=0:
            flag = 1
    if flag == 0: #assign it NOUN
        cstate = 'NOUN'
        scores[cstate]={}
        mx = {}
        mx['score'] = 0.0
        for pstate in pstates:#previous states
            tk = tk.lower() #case insensitive
            try:
                emission = float(10)/float(ct[cstate]) #Hardcoded emission here
            except KeyError:
                emission = 0
            try:
                transmission = float(tr[cstate+'_'+pstate])/float(ct[pstate])
            except KeyError:
                transmission = 0

            if itk>0:
                score = emission * transmission * stokens[itk - 1][pstate]['score']
            else:
                score = emission * transmission

            if score>mx['score']:
                mx['score'] = score
                mx['tag'] = pstate
        scores[cstate] = mx

    stokens += [scores]

#print stokens
mx = 0.0
for i in stokens[len(tokens)-1]:
    #print stokens[len(tokens)-1][i]
    if stokens[len(tokens)-1][i]['score'] > mx:
        mxtag = i
        ptag = stokens[len(tokens)-1][i]['tag']

ptag = mxtag
tagset = [ptag]
for i in range(len(stokens))[::-1][:-1]:
    ptag = stokens[i][ptag]['tag']
    tagset += [ptag]

tagset = tagset[::-1]
print tagset

