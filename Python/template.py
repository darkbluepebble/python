import os

def get_template_path(path):
	file_path = os.path.join(os.getcwd(),path)
	print(file_path)
	return file_path

def get_template(path):
	file_path=get_template_path(path)
	return open(file_path).read()

def render_context(template_string,context):
	return template_string.format(**context)

file_="template\message.txt"
file_html="template\message.html"
template=get_template(file_)
template_html=get_template(file_html)
context={
	"name":"Hazel Blake",
	"date":"02/01/19",
	"amount":"$250"
}
print(render_context(template,context))
print(render_context(template_html,context))
