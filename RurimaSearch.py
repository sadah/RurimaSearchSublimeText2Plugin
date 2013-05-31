import sublime, sublime_plugin
import webbrowser

class RurimaSearchCommand(sublime_plugin.TextCommand):
	def on_done(self, word):
		url = "http://doc.ruby-lang.org/ja/search/query:" + word + "/"
		webbrowser.open_new(url)

	def run(self, edit):
		self.view.window().show_input_panel('Search Rurema: ', '', self.on_done, None, None)
