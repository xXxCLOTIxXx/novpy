import novpy
import pyglet

main_scene = novpy.scene()


class scene_2(novpy.scene):

	def on_key_release(self, symbol, modifiers):
		if symbol == novpy.KEYS.SPACE:
			self.screen.switch_to_previous_scene()
			print(f"previous scene set [index: {self.screen.current_scene_index()}]")

	def on_draw(self):
		lbl = pyglet.text.Label('Scene 2',
							font_name='Times New Roman',
							font_size=36,
							x=200, y=200,
							anchor_x='center', anchor_y='center')
		lbl.draw()


class scene_1(novpy.scene):
	
	def on_key_release(self, symbol, modifiers):
		if symbol == novpy.KEYS.SPACE:
			self.screen.switch_to_next_scene()
			print(f"next scene set [index: {self.screen.current_scene_index()}]")
	
	def on_draw(self):
		lbl = pyglet.text.Label('Scene 1',
							font_name='Times New Roman',
							font_size=36,
							x=200, y=200,
							anchor_x='center', anchor_y='center')
		lbl.draw()




config = novpy.engine_config(
	full_screen=False,
	icon_path="icon.png",
	title=None,
	scene=scene_1(),
	debug=True
)

engine = novpy.Engine(config=config)
engine.add_scene(scene_2())


if __name__ == "__main__":
	engine.run()