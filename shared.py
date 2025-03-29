# This files includes shared functions
import json



class shared_file:
    def save_user(self, data):
        """Save generated user data to a file."""
        data_to_save = {
            "email": data["email"],
            "password": data["password"]
        }

        try:
            with open("users.json", "r") as file:
                users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            users = []

        users.append(data_to_save)

        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)  # Add indentation for readability