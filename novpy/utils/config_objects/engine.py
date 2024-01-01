import pyglet
from PIL import ImageGrab

from ...scene import scene

class screen:
	#screen = pyglet.window.get_platform().get_default_display().get_default_screen()

	width, height = ImageGrab.grab().size
	windowed_width, windowed_height = int(width/100*80), int(height/100*80)

	windowed_size = (windowed_width, windowed_height)
	full_size = (width, height)
	size = full_size

	title = "novpy engine🕹"
	icon = None
	full_screen = True
	allow_resize = True
	FPS_MAX = 60


	def resize(self, screen: pyglet.window.Window = None, size: tuple = None, reset_mode: bool = True, window_positon: tuple = None) -> tuple:

		if size:
			self.width, self.height = size
			self.windowed_width, self.windowed_height = int(self.width/100*80), int(self.height/100*80)
			self.windowed_size = (self.windowed_width, self.windowed_height)
			self.full_size = (self.width, self.height)

		if reset_mode:
			self.full_screen=False if self.full_screen is True else True
			self.size = self.full_size if self.full_screen else self.windowed_size


		if screen:
			screen.set_fullscreen(self.full_screen)
			if self.full_screen is False:screen.set_size(self.size[0], self.size[1])
		return self.size

class engine_config:
	screen = screen()
	scene = None
	resmon = False
	

	def __init__(self, scene: scene, title: str = None, allow_resize: bool = False, full_screen: bool = True, fps_max: int = 60, icon_path: str = None, engine_hotkeys: bool = True, debug: bool = False):
		self.debug = debug
		if title:self.screen.title=title
		self.screen.allow_resize=allow_resize
		self.screen.full_screen=full_screen
		if full_screen is False:
			self.screen.size=self.screen.windowed_size
		self.screen.FPS_MAX=fps_max
		if icon_path:self.screen.icon = pyglet.resource.image(icon_path)
		self.scene = scene
		self.use_hotkeys = engine_hotkeys