from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    text = request.GET['fulltext']
    word_list = text.split()
    word_dict = {i: word_list.count(i) for i in word_list}
    word_dict_list = word_dict.items()
    sorted_dict = sorted(word_dict_list, key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {
        'word_count': len(word_list),
        'fulltext': text,
        'max_word_dict': max(word_dict, key=word_dict.get),
        'word_dict': sorted_dict
    })