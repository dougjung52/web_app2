FILE_PATH = "todo_items.txt"

def parse(feet_inches):
  parts = feet_inches.split(" ")
  feet = float(parts[0])
  inches = float(parts[1])
  return {"feet": feet, "inches": inches}

def get_todos(file_path=FILE_PATH):

	""" Read a text file and return the list of todo items

	:param file_path:
	:return:
	"""

	with open(file_path, 'r') as fd:
		todos = fd.readlines()
	return todos

def write_todos(todos, file_path=FILE_PATH):

	with open(file_path, 'w') as fd:
		fd.writelines(todos)

if __name__ == "__main__":
	print("****** You are executing DIRECTLY this module!!! ******")
	print(get_todos())
