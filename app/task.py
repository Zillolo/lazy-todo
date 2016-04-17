import logging


class Task():
    _collection = "tasks"

    def __init__(self, text):
        self.id = None
        self.text = text
        self.logger = logging.getLogger("default")

    def save(self, db):
        if db is None:
            self.logger.warn("Save with 'None' database.")
            raise ValueError("Database may not be None.")

        tasks = db.collection(self._collection)
        if not tasks.exists():
            self.logger.info("Collection 'tasks' was created.")
            tasks.create()

        if self.id is None:
            self.id = tasks.store({"text": self.text}, return_id=True)
            self.logger.debug(
                "An entry has been created. ID: {0}".format(self.id))
        else:
            tasks.update(self.id, {"text": self.text})
            self.logger.debug(
                "An entry has been updated. ID: {0}".format(self.id))
