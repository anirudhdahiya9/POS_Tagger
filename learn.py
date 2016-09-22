from nltk.corpus import brown
import pickle

tr = {}
em = {}
ct = {}


for sent in (brown.tagged_sents(tagset='universal')):
    prevtag = 'start'
    for ind, wrd in enumerate(sent):
        tag = wrd[1]

        try:
            tr[tag+'_'+prevtag]  += 1
        except KeyError:
            tr[tag+'_'+prevtag] = 1
        prevtag = tag
        try:
            em[(wrd[0].lower())+'_'+tag] += 1
        except KeyError:
            em[(wrd[0].lower())+'_'+tag] = 1
        try:
            ct[tag] += 1
        except KeyError:
            ct[tag] = 1

ct['start']  = len(brown.tagged_sents())
print(len(ct))
print ct.keys()

pickle.dump(tr, open('tr.p', 'wb'))
pickle.dump(em, open('em.p', 'wb'))
pickle.dump(ct, open('ct.p', 'wb'))
