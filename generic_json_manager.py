import json
from pathlib import Path


class GenericJSONManager:

    # Generic Json file manager.

    # Example usage
    #data = {
    #    "name": "Alice",
    #    "age": 28,
    #    "skills": ["Python", "Machine Learning", "Data Science"]
    #}
    #GenericJSONManager.create_json("user_data.json", data)

    @staticmethod
    def create_json(file_path, data, overwrite=False):
        file_path = Path(file_path)

        # Ensure the directory exists
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # If the file exists and overwrite is False, raise an error
        if file_path.exists() and not overwrite:
            raise FileExistsError(f"File '{file_path}' already exists.")

        try:
            with file_path.open("w", encoding="utf-8") as file:
                # Dumps data.
                json.dump(data, file, indent=4, default=str)
        except TypeError as e:
            raise TypeError(f"Unable to serialize data: {e}")

    @staticmethod
    def read_json(file_path):
        file_path = Path(file_path)

        if not file_path.exists():
            print(f"Error: File '{file_path}' not found.")
            return None  # File doesn't exist

        try:
            # TRY TO OPEN
            with file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                # IF NOT DICTONARY, RETURN NULL
                return data if isinstance(data, dict) else {}
        except json.JSONDecodeError:
            # Bad JSON
            print(f"Error: File '{file_path}' contains invalid JSON.")
            return None
        except PermissionError:
            # PERMISSION
            print(f"Error: Permission denied for file '{file_path}'.")
            return None
        except Exception as e:
            # ELSE
            print(f"Error reading '{file_path}': {e}")
            return None

    @staticmethod
    def update_json(file_path, new_data):
        # Not 100% flushed out
        file_path = Path(file_path)
        existing_data = GenericJSONManager.read_json(file_path) or {}
        existing_data.update(new_data)
        GenericJSONManager.create_json(file_path, existing_data)

    @staticmethod
    def delete_json(file_path):
        # Not 100% flushed out
        file_path = Path(file_path)
        if file_path.exists():
            file_path.unlink()