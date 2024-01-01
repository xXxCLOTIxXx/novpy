
class warn:
    debug = False

    def __init__(self, debug_mode: bool = False):
        if debug_mode is True:self.debug = debug_mode

    def log(self, message: str):
        print(message)
    
    def warning(self, message: str, exception: Exception):
        if self.debug is False: raise exception(message)
        print(f"[WARNING] {message}")