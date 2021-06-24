from django.forms import ModelForm
from .models import Assessment, Respondent, BinaryLogisticRegression, GeneralizedAnxietyDisorder, Symptoms


class AssessmentForm(ModelForm):
	class Meta:
		model = Assessment
		fields = '__all__'

class RespondentForm(ModelForm):
	class Meta:
		model = Respondent
		fields = '__all__'

class AnxietyForm(ModelForm):
	class Meta:
		model = GeneralizedAnxietyDisorder
		fields = '__all__'

class PredictorForm(ModelForm):
	class Meta:
		model = BinaryLogisticRegression
		fields = '__all__'

class SymptomsForm(ModelForm):
	class Meta:
		model = Symptoms
		fields = '__all__'