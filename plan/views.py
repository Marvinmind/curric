from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from plan.models import Section, ModuleSelections, Module, Studyplan
from plan.service import constructSectionTree
from plan.forms import TestForm

def showplan(request):
	a = Section.objects.get(name='a')
	studyplan = Studyplan.objects.all()[0]
	selections = studyplan.moduleselections_set.all()
	tree = constructSectionTree(a,selections)
		
	return render_to_response('base.html', {'sections': tree})

def editplan(request):
	if request.method == 'POST':
		form = TestForm(request.POST)

		# Have we been provided with a valid form?
		if form.is_valid():
			modules = []
			for moduleId in form.cleaned_data['stuff']:
				modules.append(Module.objects.get(id=moduleId))
			return HttpResponse(form.cleaned_data['section'])
	root = Section.objects.get(name='a')
	form = TestForm(initial={'section': 'aCertainSection'})

	return render_to_response('editPlan.html', {'root':root, 'form':form})

# Create your views here.
