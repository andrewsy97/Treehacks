# visualization tools for conversation summerisation.
from tornado import (ioloop, web)
import simplejson as json

#from segmentation.cluster import spectral_clustering
#messages = [
#    '''
#    Don't forget it's Valentine's Day tomorrow!!
#                    Put your name down if you wanna meet your hacker valentine this weekend
#    ''',
#    '''
#    I would like to celebrate Valentine's Day with tea!
#    ''',
#    '''
#    which parrot mini drone?
#    I\u2019ve had some success using this with a Parrot Spider mini drone:
#    '''
#]
#labels = spectral_clustering(messages, num_clusters=2)

# start syncing threads.
try:
    from .source.slack import start_sync as start_slack_sync
    start_slack_sync(15)
except Exception as e:
    print '[server] error: ', e.message

SERVER_ROOT = 'visualize'

class SegmentationHandler(web.RequestHandler):
    def get(self):
        self.render('segmentation.html', data=json.dumps({
                    'messages': messages,
                    'labels': list([int(label) for label in labels])
                }))


handlers = [
    (r"/(.*\.jpg)", web.StaticFileHandler, {"path": SERVER_ROOT + "/frontend/"}),
    (r"/(.*\.png)", web.StaticFileHandler, {"path": SERVER_ROOT + "/frontend/"}),
    (r"/(.*\.css)", web.StaticFileHandler, {"path": SERVER_ROOT + "/frontend/css/"}),
    (r"/(.*\.js)", web.StaticFileHandler, {"path": SERVER_ROOT + "/frontend/js/"}),
    # main routes.
    (r"/segmentation", SegmentationHandler),
]

settings = {
    "autoreload": True,
    "debug": True,
    "template_path": SERVER_ROOT + "/frontend/template"
}


