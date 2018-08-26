import Normalizer.Normalizer_Trash_removal as normalizer
import Ranking.rank as rank
import Source_Analyzes.analize as aSource
from sklearn import svm
import numpy as np
import  json

from tkinter import filedialog

words_to_rank = ['trump', 'say', 'clinton','s',
                 'would','peopl','state','debat',
                 'campaign', 'hillari', 'one', 'presid',
                 'new','like','republican','donald',
                 'us','obama','time','also',
                 'polic','go','democrat','year',
                 'get','support','report','think',
                 'nation','make','offic','know',
                 'first','identi','vote','call',
                 'even','american','nt','could',
                 'candid','polit','elect','black',
                 'voter','countri','want','told',
                 'day','right','attack','use',
                 'work','last','former','million',
                 'many','two','continu','news',
                 'ask','take','show','white',
                 'nomine','york','point','back',
                 'week','way','cnn','question',
                 'monday','hous','poll','made',
                 'percent','well','look','see',
                 'come','thing','need','issu',
                 'senat','night','group','accord',
                 'stori','law','live','tri'
                 'parti','ad','polici','email',
                 'includ','america','public','person',
                 'citi','man','govern','help',
                 'bill','talk','2016','unit',
                 'believ','offici','anoth','fact',
                 'good','famili','releas','world',
                 'much','media','month','run',
                 'may','race','comment','plan',
                 'recent','tax','interview','put',
                 'statement','still','court','realli',
                 'a','bush','claim','cet',
                 'chang','depart','secur','communiti',
                 'gop','kill','tuesday','secretari',
                 'shoot','video','never','war',
                 'watch','septemb']


def rank_text():
    inputPath = filedialog.askopenfilename()
    jsonStr = open(inputPath).read()
    data_json = json.loads(jsonStr)
    allText = ""
    allTitles = ""
    X_train = []
    for registry in data_json:
        allText = allText + registry['text']
    # rankeia e plota
    distToPlot = rank.freqDist(allText)
    distToPlot.plot(200)


def rank_title():
    inputPath = filedialog.askopenfilename()
    jsonStr = open(inputPath).read()
    data_json = json.loads(jsonStr)

    allTitles = ""
    X_train = []
    for registry in data_json:
        allTitles = allTitles + registry['title']
    # rankeia e plota
    distToPlot = rank.freqDist(allTitles)
    distToPlot.plot(20)


#rank_text()
#normaliza

inputPath = filedialog.askopenfilename()
jsonStr = open(inputPath).read()
data_json = json.loads(jsonStr)

X_train = []
for registry in data_json:
    #aSource.analizesSource(registry)
    wordCount = rank.get_key_words_count(registry['text']+registry['title'], words_to_rank)
    print ("append ", wordCount)
    X_train.append(np.asarray(wordCount))
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train)

inputPath = filedialog.askopenfilename()
jsonStr = open(inputPath).read()
data_json = json.loads(jsonStr)
count = 0
correct=0
for registry in data_json:
    count = count+1
    test = []
    wordCount = rank.get_key_words_count(registry['text'],
                                         words_to_rank)
    test.append(np.asarray(wordCount))
    result = clf.predict(test)
    if result[0]<0:
        print ('seems false.')
        correct = correct+1
    else:
        print ('seems true.(wrong)')

print ('accuracy', correct/count)

