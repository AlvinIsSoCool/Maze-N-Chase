class ThemeManager:
	def __init__(self, themes, start_name=None):
		self.names = [name for name, _ in themes]
		self.themes = [theme for _, theme in themes]
		
		if start_name in self.names:
			self.index = self.names.index(start_name)
		else:
			self.index = 0

		self.theme = self.themes[self.index]

	def set_theme(self, theme):
		if self.theme is not theme: 
			self.theme = theme
			return False
		return True

	def next_theme(self):
		self.index = (self.index + 1) % len(self.themes)
		self.set_theme(self.themes[self.index])
		return self.theme

	def prev_theme(self):
		self.index = (self.index - 1) % len(self.themes)
		self.set_theme(self.themes[self.index])
		return self.theme