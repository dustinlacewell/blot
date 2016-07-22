import os
import re

class BasicLoader(object):
    def __init__(self, path, excludes=[], includes=[]):
        self.path = path
        self.excludes = excludes
        self.includes = includes

    def find_files(self):
        for dirpath, dirs, files in os.walk(self.path, followlinks=True):
            for filename in files:
                path = os.path.join(dirpath, filename)
                if self.check_path(path):
                    yield path

    def check_path(self, path):
        for exclusion in self.excludes:
            if re.search(exclusion, path) is not None:
                for inclusion in self.includes:
                    if re.search(inclusion, path) is not None:
                        break
                else:
                    break
        else:
            return True

    def load(self):
        files = self.find_files()
        for path in files:
            yield path
