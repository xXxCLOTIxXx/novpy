from .utils.exceptions.scene_exceptions import (
	NoPreviousScenes,
	NoNextScenes,
	IncorrectSceneIndex
)

class scene:

	def on_select(self, screen):
		self.screen = screen

	def on_resize(self, width, height):
		pass

	def on_draw(self):
		pass
			
	def on_key_press(self, symbol, modifiers):
		pass

	def on_key_release(self, symbol, modifiers):
		pass

	def on_text(self, text):
		pass
		
	def on_mouse_motion(self, x, y, dx, dy):
		pass

	def on_mouse_press(self, x, y, button, modifiers):
		pass

	def on_mouse_release(self, x, y, button, modifiers):
		pass

	def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
		pass

	def on_mouse_enter(self, x, y):
		pass

	def on_mouse_leave(self, x, y):
		pass
	
	def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
		pass


class history:
	current_scene = None
	
	def __init__(self, curent_scene: scene = None):
		self.scenes = [curent_scene]
		self.set_scene(self.scenes[0])

	def add_scene(self, scene: scene, set_as_current_scene: bool = False) -> scene:
		self.scenes.append(scene)
		if not self.current_scene or set_as_current_scene is True:
			self.set_scene(scene)
		return self.current_scene


	def current_scene_index(self) -> int:
		return self.scenes.index(self.current_scene)

	def switch_to_previous_scene(self) -> scene | None:
		current_index = self.current_scene_index()
		if current_index > 0:
			self.set_scene(self.scenes[current_index - 1])
			return self.current_scene
		
		self.notifier.warning(f"No previous scenes. Current scene: {self.current_scene_index()}, total scenes: {len(self.scenes)-1}", NoPreviousScenes)
		return None

	def switch_to_next_scene(self) -> scene | None:
		current_index = self.current_scene_index()
		if current_index < len(self.scenes) - 1:
			self.set_scene(self.scenes[current_index + 1])
			return self.current_scene
		
		self.notifier.warning(f"No next scenes. Current scene: {self.current_scene_index()}, total scenes: {len(self.scenes)-1}", NoNextScenes)
		return None

	def switch_to_scene_by_index(self, index: int) -> scene | None:
		if index < len(self.scenes):
			self.set_scene(self.scenes[index])
			return self.current_scene
		
		self.notifier.warning(f"Incorrect scene index. Current scene: {self.current_scene_index()}, total scenes: {len(self.scenes)-1}", IncorrectSceneIndex)
		return None


	def set_scene(self, scene: scene):
		self.current_scene = scene
		self.current_scene.on_select(self)