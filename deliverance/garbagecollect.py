"""
For https://projects.openplans.org/deliverance/ticket/22
"""

import gc

class GarbageCollectingMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        res = self.app(environ, start_response)

        n = gc.collect()        
        if n and 'deliverance.log' in environ:
            environ['deliverance.log'].debug(
                self,
                'Garbage-collected %s unreachable objects' % n)

        return res
