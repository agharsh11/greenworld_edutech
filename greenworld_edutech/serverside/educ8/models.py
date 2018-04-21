from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Student(models.Model):
	first_name=models.CharField(max_length=20)
	middle_name=models.CharField(max_length=20,blank=True)
	last_name=models.CharField(max_length=20)
	student_img=models.CharField(max_length=1000)
	registration_date = models.DateField()
	year_of_birth=models.IntegerField()
	birth_date=models.DateField(blank=True)

	GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	aadhar= models.CharField(max_length=12,blank=True,validators=[RegexValidator(r'^\d{12}$','Number must be 12 digits', 'Invalid aadhaar')], unique=True)

	def __str__(self):
		return "name: "+ self.first_name + " " + self.middle_name + " " + self.last_name
	def as_json(self):
		return dict( student_id = self.id,first_name = self.first_name,last_name=self.last_name,student_img=self.student_img)

class School(models.Model):
	school_name=models.CharField(max_length=20)
	school_type=models.CharField(max_length=20)
	study_medium=models.IntegerField()
	def __str__(self):
		return "name: "+ self.school_name
	def as_json(self):
		return dict( school_id = self.id,school_name = self.school_name,school_type=self.school_type,study_medium=self.study_medium)

class ScholasticDetail(models.Model):
    regular_to_school = models.BooleanField()
    current_class = models.IntegerField()
    class_last_year = models.IntegerField()
    current_school = models.ForeignKey(School, on_delete=models.CASCADE)
    years_in_current_school = models.IntegerField()
    current_school_shift = models.IntegerField()
    is_english_subject = models.BooleanField()
    break_more_than_three_weeks = models.BooleanField()
    last_grade_dropout = models.IntegerField(blank=True)
    is_private_tuition = models.BooleanField()
    tuition_fees = models.FloatField()
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
    	return self.student_id.first_name + " : " + self.current_school.school_name
    def as_json(self):
    	return dict(regular=self.regular_to_school,student_id=self.student_id.id,school_id=self.current_school.id,is_english_subject=self.is_english_subject)

