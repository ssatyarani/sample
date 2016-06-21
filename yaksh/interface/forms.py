from django import forms
from models import *
class MultipleChoiceQuestionForm(forms.ModelForm):
		class Meta:
			model = MultipleChoiceQuestion
			fields = [
					"title",
					"text",
					"language",
					"marks",
					"status",
					"no_of_inputs",
				     ]

class CodeQuestionForm(forms.ModelForm):
	    class Meta:
	    	model = CodeQuestion
	    	fields = [
	    	       "title",
	    	       "text",
	    	       "language",
	    	       "marks",
	    	       "status",
	    	       "function_name",
	    	 		 ]

class InputForm(forms.ModelForm):
		class Meta:
			model = Input
			fields = [
					"_type",
					"value",
					]


class OutputForm(forms.ModelForm):
		class Meta:
			model = Output
			fields = [
					"_type",
					"value",
					]


'''class TestCaseForm(forms.ModelForm):
	    class Meta:
	    	model = TestCase
	    	fields = [
	    	       "no_of_inputs",
	    	       "no_of_outputs",
	    	       
	    	         ]'''
	    			    	
