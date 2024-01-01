import pyglet
KEYS = pyglet.window.key




class events:
	current_scene = None

	#MONITOR

	def on_resize(self, width, height):
		if self.current_scene:
			self.current_scene.on_resize(width, height)

	def on_draw(self):
		self.clear()
		if self.current_scene:
			self.current_scene.on_draw()



	#KEYBOARD
	"""	
	def on_key_press(self, symbol, modifiers):
		if self.current_scene:self.current_scene.on_key_press(symbol, modifiers)
	"""

	def on_key_release(self, symbol, modifiers):
		if self.engine_config.use_hotkeys:self.hot_keys(symbol)
		if self.current_scene:self.current_scene.on_key_release(symbol, modifiers)


	"""
	def on_text(self, text):
		if self.current_scene:self.current_scene.on_text(text)
	"""


	#MOUSE
		
	def on_mouse_motion(self, x, y, dx, dy):
		if self.current_scene:self.current_scene.on_mouse_motion(x, y, dx, dy)

	def on_mouse_press(self, x, y, button, modifiers):
		if self.current_scene:self.current_scene.on_mouse_press(x, y, button, modifiers)

	def on_mouse_release(self, x, y, button, modifiers):
		if self.current_scene:self.current_scene.on_mouse_release(x, y, button, modifiers)

	def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
		if self.current_scene:self.current_scene.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

	def on_mouse_enter(self, x, y):
		if self.current_scene:self.current_scene.on_mouse_enter(x, y)

	def on_mouse_leave(self, x, y):
		if self.current_scene:self.current_scene.on_mouse_leave(x, y)

	def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
		if self.current_scene:self.current_scene.on_mouse_scroll(x, y, scroll_x, scroll_y)