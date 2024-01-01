"""

This library is under development. It will make it easier for you to create games (mostly novels) in Python.
The engine runs on the pyglet library, so you can use its functions directly where necessary.
All examples can be found in the examples folder on the project's GitHub.
An example of a starting point for game development::

    import novpy
    class my_scene(novpy.scene):
        pass

    config = novpy.engine_config(
        full_screen=False,
        curent_scene=my_scene()
    )

    engine = novpy.Engine(config=config)
    if __name__ == "__main__":
        engine.run()
"""





from .utils.config_objects.engine import engine_config
from .engine import Engine
from .scene import scene
from .utils.events import KEYS
