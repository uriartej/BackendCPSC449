import urllib.parse


database_file_path = "/home/juanuriarte/Project1/Updated Database Project 1.db"

encoded_file_path = urllib.parse.quote(database_file_path, safe = "/:")
DATABASE_URL = f"sqlite:///{encoded_file_path}"