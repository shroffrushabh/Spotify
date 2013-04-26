#!/usr/bin/python

import sys,StringIO

def parseInput():
        testcases = StringIO.StringIO(raw_input())
        line0 = testcases.readline()
        length = int(line0.split(' ')[0])

        if int(length) == 0:
                return
        numOfResults = int(line0.split(' ')[1])

        lines = []
        for i in range(length):
                lines.append(StringIO.StringIO(raw_input()).readline())
        processData(length,numOfResults,lines)

def processData(length,numOfResults,lines):
        res1=[]
        res2=[]
        for i in range(0,int(length)):
                temp = lines[i].split(' ')
                res1.append(temp[1])
                res2.append(float(temp[0]) * (i+1) / (float(length)))

        res = {}
        for i in range(len(res1)):
                if res.has_key(res2[i]):
                        res[res2[i]].append(res1[i])
                else:
                        res[res2[i]]=[res1[i]]

        for key in sorted(res,reverse=True):
                if numOfResults == 0:
                        break

                if len(res[key]) == 1:
                        sys.stdout.write(res[key][0]+"\n")
                        numOfResults-=1
                else:
                        if len(res[key]) <= numOfResults:
                                for elm in res[key]:
                                        sys.stdout.write(elm+"\n")
                                        numOfResults-=1
                        else:
                                for i in range(numOfResults):
                                        sys.stdout.write(res[key][i]+"\n")
                                        numOfResults-=1

if __name__ == "__main__":
        parseInput()




