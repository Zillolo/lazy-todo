import mongoengine

# Open a connection to the MongoDB database, to be shared throughout the
#   application.
db = mongoengine.connect('lazy', host='127.0.0.1', port=27017)
