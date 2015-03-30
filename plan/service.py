from plan.models import Module, Section, Studyplan, ModuleSelections

def selectModuleInSection(module, section, studyplan):
	moduleSelections = studyplan.moduleselections_set.all()
	sectionsInStudyplan = []
	for element in moduleSelections:
		sectionsInStudyplan.append(element.section)
	#look if module already exists
	for selection in moduleSelections:
		if selection.module == module:
			print('already in selections')
	#look if module belongs to section
	
	#look whether section is a leaf
	
	#look if incompatible section has been selected
	currentSection = section
	incompSections = []


	while(currentSection.parent):
		while(not currentSection.parent.exclusive_subsections.exists()):
			currentSection = currentSection.parent
		for sister in currentSection.parent.exclusive_subsections.all():
			if(sister != currentSection):
				incompSections += getAllChildrenPlusNode(sister)
		currentSection = currentSection.parent
	
	for incompSection in incompSections:
		print('an incompatibel one: '+incompSection.name)
		if incompSection in sectionsInStudyplan:
			print('this Section is incompatible with another selected section')
			#throw exception
		else:
			ModuleSelections.objects.create(module=module, section=section, studyplan=studyplan)
		
def getAllChildrenPlusNode(node):
	print('called with node '+node.name)
	sections =[]
	for child in node.mandatory_subsections.all()  | node.exclusive_subsections.all():
		if(not (child.mandatory_subsections.exists() or child.exclusive_subsections.exists())):
			sections.append(child)
		else:
			return sections.append(getAllChildrenPlusNode(child))
	sections.append(node)
	return sections

def constructSectionTree(root, selections):
	tree = Selection(root)
	for element in selections:
		hook = findAncestorInTree(tree, element.section)
		print('erster vorfahre ist: '+hook.node.name)
		if hook.node == element.section:
			hook.modules.append(element.module)
		else:
			currentSelection = Selection(element.section)
			currentSelection.modules.append(element.module)
			while not currentSelection.node.parent == hook.node:		
				newSelection = Selection(currentSelection.node.parent)
				newSelection.children.append(currentSelection)
				currentSelection = newSelection
			hook.children.append(currentSelection)		
	return tree
	
def findAncestorInTree(root, section):
	ancestor = False
	currentSection = section
	while not ancestor:
		ancestor = findInTree(root, currentSection)
		currentSection = currentSection.parent
	return ancestor
	
def findInTree(root, section):
	if root.node==section:
		return root
	elif not root.children:
		return False
	else:
		for child in root.children:
			if findInTree(child, section):
				return child
		return False
		
class Selection():
	def __init__(self, section):
		self.node = section
		self.children = []
		self.modules = []

