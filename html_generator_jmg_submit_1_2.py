def gen_lesson_html(lesson_title):
	html_text_1 = '''
	<h2 class="Lesson">''' + lesson_title
	html_text_2 = '''</h2>'''
	lesson_html = html_text_1 + html_text_2
	return lesson_html

def gen_module_html(module_title, notes):
	html_text_3 = '''
		<div class="Module"> 
		''' + module_title
	html_text_4 = '''
		</div>
		<div class="Notes">
		''' + notes
	html_text_5 = '''
		</div>
	</div>'''

	full_html_text = html_text_3 + html_text_4 + html_text_5

	return full_html_text

def get_title(module):
	start_location = module.find('MODULE:')
	end_location = module.find('NOTES:')
	title = module[start_location+8 : end_location-1]
	return title

def get_notes(module):
	start_location = module.find('NOTES:')
	notes = module[start_location+7 :]
	return notes

def get_lesson_title(lesson):
	start_location = lesson.find('LESSON:')
	end_location = lesson.find('MODULE:')
	lesson_title = lesson[start_location+8 : end_location-1]
	return lesson_title

def get_mod_count(text, module_number):
	counter = 0
	while counter < module_number:
		counter = counter + 1
		next_module_start = text.find('MODULE:')
		next_module_end = text.find('MODULE:' , next_module_start + 1)
		module = text[next_module_start:next_module_end]
		text = text[next_module_end:]
	return module

def get_lesson_text(text, lesson_number):
	LessonCounter = 0
	while LessonCounter < lesson_number:
		LessonCounter = LessonCounter + 1
		next_lesson_start = text.find('LESSON:')
		next_lesson_end = text.find('LESSON:' , next_lesson_start + 1)
		lesson = text[next_lesson_start : next_lesson_end]
		text = text[next_lesson_end:]
	return lesson

def generate_sub_html(text):
	current_module_number = 1
	module = get_mod_count(text, current_module_number)
	all_html = ''
	while module != '':
		title = get_title(module)
		notes = get_notes(module)
		module_html = gen_module_html(title, notes)
		all_html = all_html + module_html
		current_module_number = current_module_number + 1
		module = get_mod_count(text, current_module_number)
	return all_html



def generate_html_page(text):
	current_lesson_number = 1
	lesson = get_lesson_text(text, current_lesson_number)
	total_html = ''
	while lesson != '':
		lesson_title = get_lesson_title(lesson)
		lesson_html = gen_lesson_html(lesson_title)
		sub_html = generate_sub_html(lesson)
		total_html = total_html + lesson_html + sub_html
		current_lesson_number = current_lesson_number + 1
		lesson = get_lesson_text(text, current_lesson_number)
	return total_html
 



GEN_TEXT = '''LESSON: Structured Data
MODULE: Strings
NOTES: sequence of symbols or digits in computer programming
MODULE: Lists
NOTES:a sequence of values
MODULE: differences between lists and strings
NOTES: Lists can hold type of data (integers, characters, strings, etc) while strings can only hold a set of characters.
MODULE: Using Loops to iterate over structured data.
NOTES: loops can be utilized against lists
MODULE: Mutation
NOTES: means the value of a list can be changed after the list has been created
MODULE: Aliasing
NOTES: A way to apply a second name to a piece of data. In Python, aliasing happens whenever one variable's value is assigned to another variable
MODULE: append
NOTES: adds an expression to a list
MODULE: len
NOTES: provides the output of the number of elements in a list
LESSON: Problem Solving
MODULE: Rules
NOTES: 1. What are the Inputs?
		2. What are the outputs?
		3. Work through examples by hand
		4. Create a simple mechanical solution
		5. Develop incrementally and test as you go
		Do not optimize prematurely
MODULE: What is a computer program?
NOTES: A computer program is an organized list of instructions that define the task(s) that the programmer wants the machine to perform
MODULE: Functions
NOTES: Functions are a given mechanism for processing inputs and generating corresponding outputs.
'''


print generate_html_page(GEN_TEXT)










