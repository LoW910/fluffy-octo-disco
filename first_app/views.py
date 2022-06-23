from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.

articles = {
    'sports': "Sports Page",
    'finance': "Finance Page",
    'politics': "Politics Page",
}

def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        raise Http404("404 generic error")
        result = 'No page for that topic!'
        return HttpResponseNotFound(result) 


def num_page_view(requst, num_page):
    topics_list = list(articles.keys()) #['sports', 'finance', 'politics']
    topic = topics_list[num_page]
    return HttpResponseRedirect(topic)



def add_view(request, num1, num2):
    add_result = num1 + num2
    result = f"{num1} plus {num2} equals {add_result} "
    return HttpResponse(str(result))