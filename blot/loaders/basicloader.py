import os
import re


class BasicLoader(object):
    '''
    Includes basic loading discovery functionality featuring exlcude and include
    regular-expressions.

    Takes a path and recursively locates all of the files within it. Any paths that
    match any exclusion expressions are not returned. Any paths that match
    any inclusion expression are included regardless of whether they match an
    exclusuion.

    '''
    def __init__(self, path, excludes=[], includes=[], extensions=[]):
        self.path = path
        self.excludes = excludes
        self.includes = includes
        # add periods to extensions (since splitext returns extensions that way)
        self.extensions = ["." + e if e[0] != "." else e for e in extensions]

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
            _, ext = os.path.splitext(path)
            if not self.extensions or ext in self.extensions:
                return True

    def load(self):
        '''
        Return a list of all paths discovered and allowed by the exclusion and inclusion
        expresions.

        '''
        files = self.find_files()
        for path in files:
            yield path
