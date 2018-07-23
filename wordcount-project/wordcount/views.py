from django.http import HttpResponse
from django.shortcuts import render

import operator


def home(request):
    return render(request, 'wordcount/base.html')

def count(request):
    full_text = request.GET['full_text']

    wordlist = full_text.split()
    word_dict = {}
    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

        sorted_word_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'wordcount/count.html', {'full_text':full_text, 'count': len(wordlist), 'sorted_word_dict': sorted_word_dict})

def about(request):
    return render(request, 'wordcount/about.html')

