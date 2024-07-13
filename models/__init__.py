#!/bin/usr/python3
""" Init for the models module """


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
