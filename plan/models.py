from django.db import models
from django.contrib.auth.models import User


class Studyplan(models.Model):
	student = models.ForeignKey(User, blank=True, null=True)
	

class Module(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	number = models.IntegerField(blank=True, null=True)
	credit_points = models.IntegerField(blank=True, null=True)
	
	def __eq__(self, other): 
		return self.name == other.name and self.credit_points == other.credit_points

	
class Section(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	mandatory_subsections = models.ManyToManyField('self', blank=True, null=True, symmetrical=False, related_name='stuff')
	exclusive_subsections = models.ManyToManyField('self', blank=True, null=True, symmetrical=False, related_name='more_stuff')
	parent = models.ForeignKey('self', blank=True, null=True)
	level = models.IntegerField(blank=True, null=True)
	modules = models.ManyToManyField(Module, blank=True, null=True)
	
	def __eq__(self, other): 
		return self.name == other.name
	
class ModuleSelections(models.Model):
	module = models.ForeignKey(Module, blank=True, null=True)
	section = models.ForeignKey(Section, blank=True, null=True)
	studyplan = models.ForeignKey(Studyplan, blank=True, null=True)
	
	

	
	

# Create your models here.
