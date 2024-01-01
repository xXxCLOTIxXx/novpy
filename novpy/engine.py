import pyglet

from sys import exit

from . import engine_config
from .scene import scene, history
from .utils.warnings import warn
from .utils.events import events, KEYS

class Engine(pyglet.window.Window, history, events):

	def __init__(self, config: engine_config):
		super().__init__(config.screen.size[0], config.screen.size[1], config.screen.title, fullscreen=config.screen.full_screen, resizable=config.screen.allow_resize)
		history.__init__(self, config.scene)
		self.notifier = warn(config.debug)

		self.engine_config = config
		if self.engine_config.screen.icon:self.set_icon(self.engine_config.screen.icon)


	def hot_keys(self, symbol):
		if symbol == KEYS.F11:
			self.engine_config.screen.resize(screen=self)
		elif symbol == KEYS.F3:
			self.engine_config.resmon = False if self.engine_config.resmon is True else True		



	def run(self):
		pyglet.app.run()