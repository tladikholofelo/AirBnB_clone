#!/usr/bin/python3
"""This model initializes the package."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
