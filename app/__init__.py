import logging, mongoengine

# Open a connection to the MongoDB database, to be shared throughout the
#   application.
db = mongoengine.connect('lazy', host='127.0.0.1', port=27017)

# Create an instance of a logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)
