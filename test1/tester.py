from tag import tagger
from nltk.corpus import brown

size = len(brown.tagged_sents(tagset='universal'))/5

for i in range(5):
    tcount = 0
    count = 0
    sentcount = 0
    for j in range(i*size, ((i+1)*size)):
        #print j
        kachra = brown.tagged_sents(tagset='universal')[j]
        sent = []
        ans = []
        for wrd in kachra:
            sent += [wrd[0]]
            ans += [wrd[1]]
        sent = ' '.join(sent)
        tagseq = tagger(str(i),sent)
        for x in range(len(tagseq)):
            if tagseq[x]==ans[x]:
                count+=1
            tcount+=1
        sentcount += 1
        if sentcount%100==0:
            print (float(count)/float(tcount))*100
            print tcount
    f = open('results.txt','a')
    f.writelines(str(i) + ' : ' + str(float(count)/float(count)*100) + '\n')
    f.close()   

