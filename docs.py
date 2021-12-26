import sublime_plugin, sublime, json, os

class IntelliDocsCommand(sublime_plugin.TextCommand):
	def __init__(self, view):
		self.view = view

	def run(self, edit):
		syntax = self.view.settings().get('syntax').split('/')[-1].lower()

		if syntax == "func.sublime-syntax":
			selection = self.view.sel()[0]
			code_block = self.view.substr(selection)
			path_db = os.path.dirname(os.path.abspath(__file__)) + '//bd_docs.json'

			with open(path_db, 'r') as j:
			    json_data = json.load(j)


			try: 
				self.view.show_popup(json_data[code_block]["docs"])
			except KeyError as ke:
				self.view.show_popup("Documentation for {} not found".format(code_block))
