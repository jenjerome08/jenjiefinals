from django.shortcuts import render, redirect 
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import AssessmentForm, RespondentForm, AnxietyForm, PredictorForm, SymptomsForm


def home(request):
	samples = Assessment.objects.all()
	respondents = Respondent.objects.all()
	anxiety = GeneralizedAnxietyDisorder.objects.all()
	survey = BinaryLogisticRegression.objects.all()

	total_population = respondents.count()
	total_samples = survey.count()
	total_assessment = samples.count()

	ease = samples.filter(status='EASE').count()
	dis_ease = samples.filter(status='DIS-EASE').count()
	minimal = anxiety.filter(anxiety_level='Minimal').count()
	mild = anxiety.filter(anxiety_level='Mild').count()
	moderate = anxiety.filter(anxiety_level='Moderate').count()
	severe = anxiety.filter(anxiety_level='Severe').count()

	context = {
	'samples':samples, 
	'respondents':respondents,
	'anxiety':anxiety, 
	'survey':survey, 

	'total_population':total_population,
	'total_samples':total_samples,
	'total_assessment':total_assessment,

	'ease':ease,
	'dis_ease':dis_ease,

	'minimal':minimal,
	'mild':mild, 
	'moderate':moderate, 
	'severe':severe,
	}

	return render(request, 'anxiety/dashboard.html', context)




def data(request):
	predictor = BinaryLogisticRegression.objects.all()
	anxiety = GeneralizedAnxietyDisorder.objects.all()
	assessment = Assessment.objects.all()
	
	context = {'predictor':predictor, 'anxiety':anxiety, 'assessment':assessment}
	return render(request, 'anxiety/independentvariable.html', context)

def respondent(request, pk_test):
	respondent = Respondent.objects.get(id=pk_test)
	predictors = respondent.binarylogisticregression_set.all()
	surveys = respondent.generalizedanxietydisorder_set.all()
	samples = respondent.assessment_set.all()
	
	sample_count = samples.count()
	predictor_count = predictors.count()
	gad_count = surveys.count()
	context = {'respondent':respondent, 'predictor_count':predictor_count, 'gad_count':gad_count, 'samples':samples, 'surveys':surveys, 'predictors': predictors, 'sample_count':sample_count}
	return render(request, 'anxiety/respondent.html',context)


def createRelation(request):
	predictor = BinaryLogisticRegression.objects.all()
	predictor_respondent = predictor.count()
	form = PredictorForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = PredictorForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('create_assessment')

	context = {'form':form, 'predictor':predictor, 'predictor_respondent':predictor_respondent}
	return render(request, 'anxiety/create_predictor_form.html', context)


def createSymptoms(request):
	symptoms = Symptoms.objects.all()
	total_response = symptoms.count()
	a = symptoms.filter(a='True').count()
	b = symptoms.filter(b='True').count()
	c = symptoms.filter(c='True').count()
	d = symptoms.filter(d='True').count()
	e = symptoms.filter(e='True').count()
	f = symptoms.filter(f='True').count()
	g = symptoms.filter(g='True').count()
	h = symptoms.filter(h='True').count()
	i = symptoms.filter(i='True').count()
	j = symptoms.filter(j='True').count()
	form = SymptomsForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = SymptomsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('create_symptom')

	context = {'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f,'g':g,'h':h, 'i':i, 'j':j, 'form':form, 'symptoms':symptoms, 'total_response':total_response}
	return render(request, 'anxiety/symptoms_form.html', context)

def createQuestionnaires(request):
	anxiety = GeneralizedAnxietyDisorder.objects.all()
	gad_respondent = anxiety.count()
	form = AnxietyForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = AnxietyForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('create_predictor')

	context = {'form':form, 'gad_respondent':gad_respondent, 'anxiety':anxiety, }
	return render(request, 'anxiety/questionnaire.html', context)

def createAssessment(request):
	assessment = Assessment.objects.all()
	assessment_count = assessment.count()
	form = AssessmentForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = AssessmentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form, 'assessment':assessment, 'assessment_count':assessment_count}
	return render(request, 'anxiety/assessment_form.html', context)

def createRespondent(request):
	form = RespondentForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = RespondentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'anxiety/respondent_form.html', context)




































































def updateAssessment(request, pk):

	sample = Assessment.objects.get(id=pk)
	form = AssessmentForm(instance=sample)

	if request.method == 'POST':
		form = AssessmentForm(request.POST, instance=sample)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'anxiety/assessment_form.html', context)

def deleteAssessment(request, pk):
	sample = Assessment.objects.get(id=pk)
	if request.method == "POST":
		sample.delete()
		return redirect('/')

	context = {'item':sample}
	return render(request, 'anxiety/delete.html', context)



def updateRespondent(request, pk):

	respondent = Respondent.objects.get(id=pk)
	form = RespondentForm(instance=respondent)

	if request.method == 'POST':
		form = RespondentForm(request.POST, instance=respondent)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'anxiety/assessment_form.html', context)

def deleteRespondent(request, pk):
	respondent = Respondent.objects.get(id=pk)
	if request.method == "POST":
		respondent.delete()
		return redirect('/')

	context = {'item':respondent}
	return render(request, 'anxiety/delete_respondent.html', context)