import sublime, sublime_plugin, re, math

wh_matcher = re.compile(r'(width|height)=\"(\d*)\"');

def halveWidthHeightNum(matchobj):
	halved_num = math.ceil(int(matchobj.group(2), 10) / 2)
	halved_string = '%s="%d"' % (matchobj.group(1), halved_num)
	return halved_string

class HalfImageSizeCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		selected_region = self.view.sel()[0]
		selected_string = self.view.substr(selected_region)

		halved_string = wh_matcher.sub(halveWidthHeightNum, selected_string)

		self.view.replace(edit, selected_region, halved_string)

class HalfImageSizeLineCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		#get current caret position
		current_caret_position = self.view.sel()[0].begin()
		current_line_begin_point = self.view.line(current_caret_position).begin()
		current_line_end_point = self.view.line(current_caret_position).end()

		# selected current line charactors
		current_line_region = sublime.Region(current_line_begin_point, current_line_end_point)
		current_line_string = self.view.substr(current_line_region)

		halved_string = wh_matcher.sub(halveWidthHeightNum, current_line_string)

		self.view.replace(edit, current_line_region, halved_string)

class HalfImageSizeAllCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		# selected all charactors
		all_region = sublime.Region(0, self.view.size())
		selected_string = self.view.substr(all_region)

		halved_string = wh_matcher.sub(halveWidthHeightNum, selected_string)

		self.view.replace(edit, all_region, halved_string)
