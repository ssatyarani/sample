from interface.models import Question, MultipleChoiceQuestion, CodeQuestion, Choice, TestCase, Rating, Review, Input, Output
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from forms import *

def show_home(request):
	return render(request,"index.html",{})
	
def show_questions_stu(request):
	questions = Question.objects.all()
	
	context = {
		"question_choices" : questions,
	          }
	return render(request, "display_questions.html", context)

def show_questions_mod(request):
	questions = Question.objects.all()
	
	context = {
		"question_choices" : questions,
	          }
	return render(request, "display_questions_mod.html", context)
def add_mcquestion(request):
	
	if request.POST:
		form = MultipleChoiceQuestionForm(request.POST)
		if form.is_valid():
			instance = form.save()
		else:
			return render(request, "add_mcquestion.html", {"form": form })

		no_of_inputs = request.POST.get('no_of_inputs')
		
		for i in range(1, int(no_of_inputs)+1):
			choice_text = request.POST.get('choice'+ str(i))
			choice_correct = request.POST.get('correct'+ str(i))
			if (choice_correct==None):
					choice_correct = False
			new_choice = Choice(text=choice_text, question=instance, correct=choice_correct);
			new_choice.save()
    
		return HttpResponse("Question Added. <a href='../'>Go back</a>")
	else:
		form = MultipleChoiceQuestionForm()
		return render(request, "add_mcquestion.html", {"form": form })



def add_cquestion(request):

	if request.POST:
		form = CodeQuestionForm(request.POST)
		if form.is_valid():
			instance = form.save()
		else:
			return render(request, "untitled.html", {"form": form }) 

		no_of_testcases = request.POST.get('no_of_testcases')
		
		for i in range(1, int(no_of_testcases)+1):
			testcase_inputs = request.POST.get('no_of_inputs'+ str(i))
			testcase_outputs = request.POST.get('no_of_outputs'+ str(i))
			new_testcase = TestCase(no_of_inputs=testcase_inputs, question=instance, no_of_outputs=testcase_outputs);
			new_testcase.save()
    
		return HttpResponse("Question Added. <a href='../'>Go back</a>")
	else:
		form = CodeQuestionForm()
		return render(request, "add_cquestion.html", {"form": form })


def approve_questions(request,id=None):


	question = get_object_or_404(Question,pk=id)

	questions = Question.objects.filter(id=id)
	result_set = []	
	for ques in questions:
		ratings = Rating.objects.filter(question=ques)
		question_dict = {
			"Question" : ques,
			"Ratings" : ratings,
		                }
		result_set.append(question_dict)

	questions = Question.objects.filter(id=id)
	result_set2 = []	
	for ques in questions:
		reviews = Review.objects.filter(question=ques)
		question_dict = {
			"Question" : ques,
			"Reviews" : reviews,
		                }
		result_set2.append(question_dict)

	questions = MultipleChoiceQuestion.objects.filter(id=id)
	result_set3 = []
	for ques in questions: 
		choices = Choice.objects.filter(question=ques)
		question_dict = {
			"Question" : ques,
			"Choices" : choices,
		                }
		result_set3.append(question_dict)


	questions = CodeQuestion.objects.filter(id=id)
 	result_set4 = []
	for ques in questions:
		testcases = TestCase.objects.filter(question=ques)
		each_test = []
		for each_testcase in testcases:
			inputs = Input.objects.filter(test_cases=each_testcase)
			outputs = Output.objects.filter(test_cases=each_testcase)
			testcase = {
				"input":inputs,
				"output":outputs,
				 }
			each_test.append(testcase)
		question_dict = {
		"Question" : ques,
		"Testcases" : each_test,
		}
		
		result_set4.append(question_dict)
	
	context = {
		
		"question_ratings" : result_set,
		"question_reviews" : result_set2,
		"question_choices" : result_set3,
		"question_testcases" : result_set4,
		'question' : question,
	  		  }

	return render(request, "moderator.html", context)


def approve_questions_accept(request,id=None):
	question = get_object_or_404(Question,pk=id)
	question.approve()
	question.save()
	print question
	return HttpResponseRedirect("../")	

def show_reviews(request):	
	questions = Question.objects.all()
	result_set = []	
	for ques in questions:
		reviews = Review.objects.filter(question=ques)
		question_dict = {
			"Question" : ques,
			"Reviews" : reviews,
		                }
		result_set.append(question_dict)
	context = {
		"question_reviews" : result_set,
	          }
	return render(request, "display_review.html", context)
	
def show_ratings(request):
	questions = Question.objects.all()
	result_set = []	
	for ques in questions:
		ratings = Rating.objects.filter(question=ques)
		question_dict = {
			"Question" : ques,
			"Ratings" : ratings,
		                }
		result_set.append(question_dict)
	context = { 
		"question_ratings" : result_set,
	          }

	return render(request, "display_rating.html", context)

def add_comment(request,id):
	
	question = get_object_or_404(Question,pk=id)

	questions = Question.objects.filter(id=id)
	result_set = []	
	for ques in questions:
		reviews = Review.objects.filter(question=ques)
		question_dict = {
			"Question" : ques,
			"Reviews" : reviews,
		                }
		result_set.append(question_dict)
	

	questions = Question.objects.filter(id=id)
	result_set2 = []	
	for ques in questions:
		ratings = Rating.objects.filter(question=ques)
		question_dict = {
			"Question" : ques,
			"Ratings" : ratings,
		                }
		result_set2.append(question_dict)

	questions = MultipleChoiceQuestion.objects.filter(id=id)
	result_set3 = []
	for ques in questions: 
		choices = Choice.objects.filter(question=ques)
		question_dict = {
			"Question" : ques,
			"Choices" : choices,
		                }
		result_set3.append(question_dict)

	questions = CodeQuestion.objects.filter(id=id)
 	result_set4 = []
	for ques in questions:
		testcases = TestCase.objects.filter(question=ques)
		each_test = []
		for each_testcase in testcases:
			inputs = Input.objects.filter(test_cases=each_testcase)
			outputs = Output.objects.filter(test_cases=each_testcase)
			testcase = {
				"input":inputs,
				"output":outputs,
				 }
			each_test.append(testcase)
		question_dict = {
		"Question" : ques,
		"Testcases" : each_test,
		}
		
		result_set4.append(question_dict)
	
	context = { 
		"question_reviews" : result_set,
		"question_ratings" : result_set2,
		"question_choices" : result_set3,
		"question_testcases" : result_set4,
		'question' : question ,

	 		       }


	return render(request,'student.html', context)

def post_comment(request,id):

	if request.POST:
		comment = request.POST.get("content")
		rating = request.POST.get("rating")
		user=6
		try:
			instance = get_object_or_404(Review, reviewer=user)
			return HttpResponse("you have already commented on this question")
			
		except Exception, e:
			
			try:
				instance = get_object_or_404(Rating, user=user)
				return HttpResponse("you have already rated this question")
				
			except Exception, e:
				question = get_object_or_404(Question,pk=id)
				instance = Rating(user_id=user,question=question,rate=rating)
				instance.save()
				instance = Review(reviewer_id=user,question=question,comments=comment)
				instance.save()
				return HttpResponse("You have rated this question.!")

	else:
		return HttpResponseRedirect("../")


	
