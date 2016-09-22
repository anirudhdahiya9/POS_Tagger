from nltk.corpus import brown
import pickle

tr = {}
em = {}
ct = {}


for sent in (brown.tagged_sents()):
    prevtag = 'start'
    for ind, wrd in enumerate(sent):
        try:
            tr[wrd[1]+'_'+prevtag]  += 1
        except KeyError:
            tr[wrd[1]+'_'+prevtag] = 1
        prevtag = wrd[1]
        try:
            em[(wrd[0].lower())+'_'+wrd[1]] += 1
        except KeyError:
            em[(wrd[0].lower())+'_'+wrd[1]] = 1
        try:
            ct[wrd[1]] += 1
        except KeyError:
            ct[wrd[1]] = 1

ct['start']  = len(brown.tagged_sents())
print(len(ct))

pickle.dump(tr, open('tr.p', 'wb'))
pickle.dump(em, open('em.p', 'wb'))
pickle.dump(ct, open('ct.p', 'wb'))
