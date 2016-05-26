import json

with open("partial_index.html", "r") as f:
	main_page = f.read()

with open("todo_list.csv", "r") as f:
	todo_list = [line.strip().split("\t") for line in f if line.strip()]
#When posting make sure to remove tabs
# Todo convert from timestamp
todo_list = [{'id':l[0],'ts':l[1], 'text':l[2]} for l in todo_list]
main_page = '<html>' + main_page +"<script> data='" json.dumps(todo_list) + "' </script></html>"
print main_page