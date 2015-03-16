from django.test import TestCase
from plan.models import Section, ModuleSelections, Module, Studyplan
from plan.service import selectModuleInSection, constructSectionTree
from django.core import serializers
from plan import models

class SectionTestCase(TestCase):
	def setUp(self):
		a=Section.objects.create(name="a")
		b=Section.objects.create(name="b")
		c=Section.objects.create(name="c")
		d=Section.objects.create(name="d")
		e=Section.objects.create(name="e")
		f=Section.objects.create(name="f")
		g=Section.objects.create(name="g")
		
		b.parent = a
		c.parent = a
		d.parent = b
		e.parent = b
		f.parent = a
		g.parent = f
		
		
		a.exclusive_subsections.add(b)
		a.exclusive_subsections.add(c)
		a.exclusive_subsections.add(f)
		
		b.mandatory_subsections.add(d)
		b.mandatory_subsections.add(e)
		f.mandatory_subsections.add(g)
		
		#Modules
		module_1 = Module.objects.create(name="Ulla Modul")
		module_1.credit_points = 6
		module_2 = Module.objects.create(name="Martin Modul")
		module_2.credit_points = 6

		g.modules.add(module_2)
		g.modules.add(module_1)
		a.save()
		b.save()
		c.save()
		d.save()
		e.save()
		f.save()
		g.save()
		
		
		module_1.save()
		module_2.save()
		selection_c = ModuleSelections.objects.create(section=c)
		selection_g = ModuleSelections.objects.create(section=g)
		selection_c.module = module_1
		selection_g.module = module_2
		
		
		
		studyplan = Studyplan.objects.create()
		selection_c.studyplan = studyplan
		selection_g.studyplan = studyplan
		
		selection_c.save()
		selection_g.save()
		studyplan.save()
		
		q1 = Section.objects.all()
		q2 = ModuleSelections.objects.all()
		q3= Studyplan.objects.all()
		q4= Module.objects.all()
		data = serializers.serialize("json", list(q1)+list(q2)+list(q3)+list(q4))
		out = open("./plan/fixtures/mymodel.json", "w")
		out.write(data)
		out.close()


	def test_section_parent(self):
		d = Section.objects.get(name='d')
		current_element = d
		while(current_element.parent):
			current_element = current_element.parent
		self.assertEqual(current_element.name, 'a')
	
	def test_insert_section(self):
		studyplan = Studyplan.objects.all()[0]
		module = Module.objects.get(name="Ulla Modul")
		section = Section.objects.get(name='d')
		selectModuleInSection(module, section, studyplan)
	
	def test_treet_construction(self):
		print('start Tree Construction')
		a = Section.objects.get(name='a')
		studyplan = Studyplan.objects.all()[0]
		selections = studyplan.moduleselections_set.all()
		tree = constructSectionTree(a,selections)
		print('tree kinder: '+tree.children[0].node.name)
