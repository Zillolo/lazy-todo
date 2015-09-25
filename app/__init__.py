import configobj, logging, mongoengine, sys

# Create an instance of a logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info('Loading configuration file.')
config = configobj.ConfigObj('config.cfg')

# Open a connection to the MongoDB database, to be shared throughout the
#   application.
try:
    db = mongoengine.connect(config['Database']['db'], host = config['Database']['host'], port = int(config['Database']['port']))
except:
    logger.exception('There was an error reading the config file.')
    sys.exit(1)
