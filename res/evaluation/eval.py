import csv
csvFileToEval = open('D:\\to_eval.csv', 'rb') 
readerToEvalSet = csv.DictReader(csvFileToEval, delimiter=';', quotechar='"')
readerToEvalSetList = [x for x in readerToEvalSet]
csvFileTest = open('D:\\test_set_labels.csv', 'rb') 
readerTestSet = csv.DictReader(csvFileTest, delimiter=';', quotechar='"')
readerTestSetList = [x for x in readerTestSet]

tp = 0
tn = 0
fp = 0
fn = 0
#csvFileDev = open('D:\\development_set.csv', 'rb') 
#readerDevSet = csv.DictReader(csvFileDev, delimiter=';', quotechar='"')
#for row in readerTestSet:
#     print row['movie_name'], row['file_name'], row['goodforairplanes']
#print 'TEST SET PRINTED'
#for row in readerDevSet:
#     print row['movie_name'], row['file_name'], row['goodforairplane']
#print 'DEV SET PRINTED'

print 'To Evaluate Set length: ', len(readerToEvalSetList)
print 'Test Set length: ', len(readerTestSetList)

#matchcount = 0

for rowEval in readerToEvalSetList:
    #print rowEval['file_name']
    #print readerTestSet
    #ismatch = 0
    for rowTest in readerTestSetList:
        if rowEval['movie_name']==rowTest['movie_name']:
            #matchcount = matchcount + 1
            #print rowEval['file_name'], rowTest['file_name'], 'same movie'
            if rowEval['goodforairplanes']==rowTest['goodforairplanes']:
                if rowTest['goodforairplanes']=='1':
                    tp = tp+1
                    #ismatch = 1
                elif rowTest['goodforairplanes']=='0':
                    tn = tn+1
                    #ismatch = 1
            elif rowEval['goodforairplanes']=='1' and rowTest['goodforairplanes']=='0':
                    fp = fp+1
                    #ismatch = 1
            elif rowEval['goodforairplanes']=='0' and rowTest['goodforairplanes']=='1':
                    fn = fn+1
                    #ismatch = 1
    #if ismatch == 0:
    #    print 'nomatch ', rowEval['movie_name']
    #elif ismatch == 1:
    #    print matchcount
print 'tp', tp, 'tn', tn, 'fp', fp, 'fn', fn
precision = float(tp)/(tp+fp)
recall = float(tp)/(tp+fn)
f1 = 2.0*((precision*recall)/(precision+recall))
print 'precision', precision, 'recall', recall, 'f1 score', f1

