#buat fungsi untuk menata  dataset kedalam kamus2 / dictionary
def dataset(arr,val):
    w={}
    w['words']=arr
    w['val']=val
    return w
w1=dataset(['jokowi','calon','presiden'],1)
w2=dataset(['liga','champions'],0)
w3=dataset(['jokowi','maju','pilpres'],1)
w4=dataset(['final','liga','champions'],0)

words=[w1,w2,w3,w4]

#mencari nilai prior dr Yes dan No
yesP=float()
noP=float()
index=float(len(words))

diff_words=[]
count_word={'yes':0,'no':0}
count_word_yes={}
count_word_no={}
for dat in words:
    if dat['val']==1:
        yesP+=1.0
        for yes in dat['words']:
            count_word['yes']+=1
            if yes not in count_word_yes:
                count_word_yes[yes]=1
            else:
                count_word_yes[yes]+=1
    else:
        noP+=1.0
        for no in dat['words']:
            count_word['no']+=1
            if no not in count_word_no:
                count_word_no[no]=1
            else:
                count_word_no[no]+=1
    for word in dat['words']:
        if word not in diff_words:
            diff_words.append(word)
size=len(diff_words)

#mencari nilai likelihood masing-masing kata kategori dr Yes dan No
likelihoods_yes={}
likelihoods_no={}
for word in diff_words:
    word=str(word)
    if word not in count_word_yes:
        count_word_yes[word]=0
    
    if word not in count_word_no:
        count_word_no[word]=0
    likelihoods_yes[word]= (float(count_word_yes[word])+1)/(float(count_word['yes'])+float(size))
    likelihoods_no[word]= (float(count_word_no[word])+1)/(float(count_word['no'])+float(size))

print "lhood yes:",likelihoods_yes
print "lhood no:",likelihoods_no
yesP=yesP/index
noP=noP/index
print "prior yes:",yesP,"prior no:",noP

#membuat fungsi classifcation, jika Yes maka -> politik, jika no-> Olahraga
def classification(arr):
    global yesP
    global noP
    mytesting=arr
    likehood_yes=float(1.0)
    likehood_no=float(1.0)
    for test in mytesting:
        try:
            likehood_yes =(likehood_yes * likelihoods_yes[test])
            likehood_no =(likehood_no * likelihoods_no[test])
        except:
            pass
    weight_yes = likehood_yes * yesP
    weight_no = likehood_no * noP
    if weight_yes >= weight_no:
        return "politik"
    else:
        return "olahraga"
    
#percobaan fungsi yang sudah dibuat
test1=classification(['final','liga','presiden'])
print "test1:",test1

test2=classification(['jokowi','calon','presiden'])
print "test2:",test2
