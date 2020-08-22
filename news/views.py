from django.shortcuts import render

# Create your views here.
from newsapi import NewsApiClient


def news(request):
	newsapi= NewsApiClient(api_key="051517e79d5346ba8674f20c238df37c")
	topheadlines = newsapi.get_top_headlines(sources="the-times-of-india")

	articles =topheadlines['articles']

	desc =[]
	news = []
	img=[]

	for i in range (len(articles)):
		myarticles=articles[i]

		news.append(myarticles['title'])
		desc.append(myarticles['description'])
		img.append(myarticles['urlToImage'])

	mylist = zip(news, desc, img)

	return render (request,'news.html',context={"mylist": mylist})

def bbc(request):
	newsapi= NewsApiClient(api_key="051517e79d5346ba8674f20c238df37c")
	topheadlines = newsapi.get_top_headlines(sources="bbc-news")

	articles =topheadlines['articles']

	desc =[]
	news = []
	img=[]

	for i in range (len(articles)):
		myarticles=articles[i]

		news.append(myarticles['title'])
		desc.append(myarticles['description'])
		img.append(myarticles['urlToImage'])

	mylist = zip(news, desc, img)

	return render (request,'bbc.html',context={"mylist": mylist})