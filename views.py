from django.http import HttpResponse
from django.shortcuts import render
import operator
from . import counter 

def home(request):
    return render(request,'index.html',{'Key1':'I am python expert programmer'})

def result(request):
    article = request.GET['article']
    var_dict,word_count = counter.count(article)
    # words = article.split()
    # word_count = len(words)
    # dict_words = {}
    # for word in words:
    #     if word in dict_words:
    #         dict_words[word] += 1
    #     else:
    #         dict_words[word] = 1
    # var_dict = sorted(dict_words.items(),key=operator.itemgetter(1),reverse=True)
    # age = request.GET['user_age']
    # name = request.GET['user_name']
    # message = f'Assalam U Alikum, {name}, I am {21} years old'
    return render(request, 'result.html',{'article':article,'word_count':word_count,'dict_words':var_dict})

# def downloads(request):
#     return HttpResponse('<h1> No Downloads File <\h1>')