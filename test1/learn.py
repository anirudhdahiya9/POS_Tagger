from nltk.corpus import brown
import pickle
import sys

tr = {}
em = {}
ct = {}

serial = int(sys.argv[1])
size = len(brown.tagged_sents(tagset='universal'))/5;

for isent, sent in enumerate(brown.tagged_sents(tagset='universal')):
    if isent >=serial*size and isent<(serial+1)*size:
        continue
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

ct['start']  = len(brown.tagged_sents())*4/5;
print(len(ct))
print ct.keys()

serial = str(serial)

pickle.dump(tr, open('tr'+serial+'.p', 'wb'))
pickle.dump(em, open('em'+serial+'.p', 'wb'))
pickle.dump(ct, open('ct'+serial+'.p', 'wb'))
print serial
