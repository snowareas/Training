from django.db import models

# Create your models here.
class Department(models.Model):
	department_ID = models.CharField(max_length = 6,primary_key = True)
	name = models.CharField(max_length = 10)

	def __str__(self):
		return self.name

class Student(models.Model):
	student_ID = models.CharField(max_length = 11,primary_key = True)
	name = models.CharField(max_length = 10)
	age = models.IntegerField(null = True)
	grade = models.FloatField(null = True)
	department = models.ForeignKey(Department, on_delete = models.CASCADE)

class Course(models.Model):
	course_ID = models.CharField(max_length = 11,primary_key = True)
	name = models.CharField(max_length = 20)
	student = models.ManyToManyField(Student,through = 'Select',through_fields = ('course','student'))

	def __str__(self):
		return self.name

class Select(models.Model):
	course = models.ForeignKey(Course, on_delete = models.CASCADE)
	student = models.ForeignKey(Student,on_delete = models.CASCADE)
	grade = models.IntegerField(null = True)

