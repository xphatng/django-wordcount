'''
Created on Jun 17, 2018

@author: phattannguyen
'''
from django.http import HttpResponse
from django.shortcuts import render
from _operator import itemgetter

def views(request):
    return HttpResponse('<head>Welcome</head><body><h1>Hello</h1></body>')

def custominfo(request):
    return render(request, 'custom.html', {'hithere': 'This is wordcount web page make by Phat'})
########
#######
def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordList = fulltext.split()
    wordDict = {}
    for word in wordList:
        if word in wordDict.keys():
            wordDict[word] = wordDict[word] +1
        else:
            wordDict[word] = 1
    count = len(fulltext.split())
    listDict = sorted(wordDict.items(), key=itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count':count, 'wordDict': wordDict, 'listDict': listDict})