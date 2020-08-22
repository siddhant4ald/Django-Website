from django.shortcuts import render
import random

words=[
	"python","java","html","programming","database","django","computer","hacker", "developer",
	"coding","angular","nodejs","engineering","javascript"


]
def rword():
	global jword
	global word
	word=random.choice(words)
	jum=random.sample(word,len(word))
	jword="".join(jum)

msg=""
count=0
def fun(request):
	rword()
	global jword , msg,count
	
	return render(request,'fun.html',{'jum_word':jword})


def check(request):
	global word, msg, jword,count

	user_ans=request.GET['ans']
	if user_ans==word:

		msg="You are genius ,Keep Goin"
		count+=1


		fun(request)

	else:
		msg="Oops Wrong Answer , Try again"
		count=0
	return render(request,'fun.html',{'jum_word':jword,'msg':msg,'count':count})
	
		
		
	