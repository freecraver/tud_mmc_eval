#!/usr/bin/env python
import csv, sys, os, os.path

# simulating the input parameters
#sys.argv = ['evaluate.py','input','output']
  
#if len(sys.argv) != 2:
#    parser.error("incorrect number of arguments")

submit_dir = os.path.join(sys.argv[1], 'res') 
truth_dir = os.path.join(sys.argv[1], 'ref')
out_dir = sys.argv[2]

#input_dir = sys.argv[1]
#output_dir = sys.argv[2]
#for local testing
#input_dir = 'D:\\Data\\Dropbox\\Context_of_Experience_complete\\codalab_draft'
#output_dir = 'D:\\Data\\Dropbox\\Context_of_Experience_complete\\codalab_draft'

#submit_dir = os.path.join(input_dir, 'res') 
#truth_dir = os.path.join(input_dir, 'ref')
#for local testing
#submit_dir = os.path.join(input_dir, 'submission') 
#truth_dir = os.path.join(input_dir, 'reference')

print submit_dir

if not os.path.isdir(submit_dir):
    print "%s doesn't exist" % submit_dir

if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    output_filename = os.path.join(out_dir, 'scores.txt')              
    output_file = open(output_filename, 'wb')
    print output_filename

    gold_list = os.listdir(truth_dir)
    for gold in gold_list:
        #print gold
        gold_file = os.path.join(truth_dir, gold)
        print gold_file
        corresponding_submission_file = os.path.join(submit_dir, gold)
        print corresponding_submission_file
        if os.path.exists(corresponding_submission_file):
            csvFileToEval = open(corresponding_submission_file, 'rb')#csvFileToEval = open('D:\\to_eval.csv', 'rb') 
            readerToEvalSet = csv.DictReader(csvFileToEval, delimiter=',', quotechar='"')
            readerToEvalSetList = [x for x in readerToEvalSet]
            csvFileTest = open(gold_file, 'rb')#csvFileTest = open('D:\\test_set_labels.csv', 'rb') 
            readerTestSet = csv.DictReader(csvFileTest, delimiter=',', quotechar='"')
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

            #print 'To Evaluate Set length: ', len(readerToEvalSetList)
            #print 'Test Set length: ', len(readerTestSetList)

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
            #print 'tp', tp, 'tn', tn, 'fp', fp, 'fn', fn
            if tp==0:
                precision=0.0
                recall=0.0
                f1=0.0
            else:
                precision = float(tp)/(tp+fp)
                recall = float(tp)/(tp+fn)
                f1 = 2.0*((precision*recall)/(precision+recall))
            #print 'precision', precision, 'recall', recall, 'f1 score', f1
            #output_file.write('Results: %s %s %s\n'%(precision, recall, f1))
    output_file.write('F1_score: %f\n Precision: %f\n Recall: %f\n' % (f1, precision, recall))
    output_file.close()
