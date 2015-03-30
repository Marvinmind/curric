from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from plan.models import Section, ModuleSelections, Module, Studyplan
from plan.service import constructSectionTree, selectModuleInSection
from plan.forms import TestForm

from django.views.decorators.cache import never_cache

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

@never_cache
def showplan(request):
	a = Section.objects.get(name='a')
	studyplan = Studyplan.objects.all()[0]
	selections = studyplan.moduleselections_set.all()
	tree = constructSectionTree(a,selections)
		
	return render_to_response('base.html', {'sections': tree})

@never_cache
def editplan(request):
	if request.method == 'POST':
		modules = []
		selected_modules_ids = request.POST.getlist('stuff')
		section = Section.objects.get(name= request.POST['section'])
		studyplan = Studyplan.objects.all()[0]

		for moduleId in selected_modules_ids:
			current_module = Module.objects.get(id=moduleId)
			modules.append(current_module)
			selectModuleInSection(current_module, section, studyplan)
		return HttpResponse(str(modules))

	forms_dict = {}
	for leaf_section in Section.objects.exclude(modules__isnull=True):
		current_list = []
		for module in leaf_section.modules.all():
			current_list.append((module.id, module.name))
		forms_dict[leaf_section.name] = TestForm(initial={'section': leaf_section.name}, modules = current_list )

	actualList = list(forms_dict.values())[0]
	root = Section.objects.get(name='a')

	return render_to_response('editPlan.html', {'root':root, 'forms':forms_dict})

# Create your views here.
