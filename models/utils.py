import os

def get_path(*paths):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, *paths)