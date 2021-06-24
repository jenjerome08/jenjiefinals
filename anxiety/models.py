from django.db import models

# Create your models here.

class Respondent(models.Model):
	name = models.CharField(max_length=200, null=True)
	GENDER = (
			('Male', 'Male'),
			('Female', 'Female'),
			) 
	gender = models.CharField(max_length=200, null=True, choices=GENDER)
	age = models.IntegerField()
	section = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	image = models.ImageField(default='default.png', blank=True)
	def __str__(self):
		return self.name

class Symptoms(models.Model):
	name = models.ForeignKey(Respondent, null=True, on_delete= models.SET_NULL)
	a = models.BooleanField("restlessness", default=False)
	b = models.BooleanField("difficulty concentrating", default=False)
	c = models.BooleanField("irritability", default=False)
	d = models.BooleanField("dizziness", default=False)
	e = models.BooleanField("tiredness", default=False)
	f = models.BooleanField("feeling sick", default=False)
	g = models.BooleanField("muscle aches", default=False)
	h = models.BooleanField("a sense of dread", default=False)
	i = models.BooleanField("headache", default=False)
	j = models.BooleanField("insomnia", default=False)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
class GeneralizedAnxietyDisorder(models.Model):
	name = models.ForeignKey(Respondent, null=True, on_delete= models.SET_NULL)
	tupc_id = models.CharField(max_length=200, null=True)
	points = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	LEVEL = (
			('Minimal', 'Minimal'),
			('Mild', 'Mild'),
			('Moderate', 'Moderate'),
			('Severe', 'Severe'),
			) 
	anxiety_level = models.CharField(max_length=200, null=True, choices=LEVEL)
	def __str__(self):
		return self.anxiety_level + ' : ' + self.tupc_id


class BinaryLogisticRegression(models.Model):
	name = models.ForeignKey(Respondent, null=True, on_delete= models.SET_NULL)
	anxiety = models.ManyToManyField(GeneralizedAnxietyDisorder)
	Binary1 = (
			('Yes', 'Yes'),
			('No', 'No'),
			)
	Binary2 = (
			('Stable', 'Stable'),
			('Unstable', 'Unstable'),
			) 
	exercise = models.CharField(max_length=200, null=True, choices=Binary1)
	computer_or_laptop = models.CharField(max_length=200, null=True, choices=Binary1)
	Living_with_family = models.CharField(max_length=200, null=True, choices=Binary1)
	internet_connection = models.CharField(max_length=200, null=True, choices=Binary2)
	main_cause = models.CharField(max_length=200, null=True, blank="I don't Know")
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return self.main_cause


class Assessment(models.Model):
	STATUS = (
			('EASE', 'EASE'),
			('DIS-EASE', 'EASE'),
			)
	name = models.ForeignKey(Respondent, null=True, on_delete= models.SET_NULL)
	predictors = models.ForeignKey(BinaryLogisticRegression, null=True, on_delete= models.SET_NULL)
	anxiety_levels = models.ForeignKey(GeneralizedAnxietyDisorder, null=True, on_delete= models.SET_NULL)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	

	def __str__(self):
		return self.status

