from locust import HttpUser, TaskSet, task, between, tag
import json
import random
import logging

# Minimal logging setup
logging.basicConfig(level=logging.INFO)

class MyTaskSet0(TaskSet):
    def on_start(self):
        logging.info("Youbloomconnect is starting")
        self.token = None  # Store authentication token
    @task(3)
    @tag("Login")
    def login(self):
        self.headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
        }

        try:
            with open("data1.json", "r") as file:
                data1 = json.load(file)

            if not data1:
                logging.info("No users found in data1.json")
                return

        except (FileNotFoundError, json.JSONDecodeError):
            logging.info("Error loading users from data1.json")
            return

        # Select a random user
        user = random.choice(data1)
        login_data = {
        "email": user["email"],
        "password": user["password"]
        }

        with self.client.post("/login",  # Ensure correct API path
                          data=json.dumps(login_data),
                          name="youbloomconnect",
                          headers=self.headers,
                          timeout=120,
                          catch_response=True) as response:
            logging.info(f"Login Response Code: {response.status_code}")
            logging.info(f"Login Response Body: {response.text}")

        if response.status_code == 200 and response.text.strip():  # Check if body is not empty
            try:
                json_response = response.json()
                self.token = json_response.get("token")

                if self.token:
                    self.headers["Authorization"] = f"Bearer {self.token}"
                    logging.info(f"Stored Token: {self.token}")
                else:
                    logging.info("No token found in response!")

            except json.JSONDecodeError:
                logging.info("Login response was not valid JSON")
        else:
            logging.info(f"Login failed with status code {response.status_code}: {response.text}")

    @task(2)
    def myshows(self):
        if not self.token:
            logging.info("No token found. Attempting login first...")
            self.login()
            if not self.token:
                logging.info("Login failed, cannot proceed to /myshows/")
                return

        logging.info(f"Using Token for /myshows/: {self.token}")

        with self.client.get("/myshows",  # Ensure correct API path
                             name="myshows",
                             headers=self.headers,  # Send Authorization header
                             timeout=120,
                             catch_response=True) as response:
            logging.info(f"MyShows Response Code: {response.status_code}")
            logging.info(f"MyShows Response Body: {response.text}")

            if response.status_code in [200, 302]:
                logging.info("My shows page loaded")
            else:
                logging.info(f"My shows page failed with status code {response.status_code}: {response.text}")
    @task(2)
    def confirmedgig(self):
        if not self.token:
            logging.info("No token found. Attempting login first...")
            self.login()
            if not self.token:
                logging.info("Login failed, cannot proceed to /confirmedgig/")
                return

        logging.info(f"Using Token for /confirmedgig/: {self.token}")

        with self.client.get("/confirmedgig",  # Ensure correct API path
                             name="confirmedgig",
                             headers=self.headers,  # Send Authorization header
                             timeout=120,
                             catch_response=True) as response:
            logging.info(f"MyShows Response Code: {response.status_code}")
            logging.info(f"MyShows Response Body: {response.text}")

            if response.status_code in [200, 302]:
                logging.info("confirmedgig page loaded")
            else:
                logging.info(f"confirmedgig page failed with status code {response.status_code}: {response.text}")
    @task(2)
    def artistsFanRating(self):
        if not self.token:
            logging.info("No token found. Attempting login first...")
            self.login()
            if not self.token:
                logging.info("Login failed, cannot proceed to /artistsFanRating/")
                return

        logging.info(f"Using Token for /artistsFanRating/: {self.token}")

        with self.client.get("/artistsFanRating",  # Ensure correct API path
                             name="artistsFanRating",
                             headers=self.headers,  # Send Authorization header
                             timeout=120,
                             catch_response=True) as response:
            logging.info(f"artistsFanRating Response Code: {response.status_code}")
            logging.info(f"artistsFanRating Response Body: {response.text}")

            if response.status_code in [200, 302]:
                logging.info("artistsFanRating page loaded")
            else:
                logging.info(f"artistsFanRating page failed with status code {response.status_code}: {response.text}")
                
    @task(2)
    def artistsSCRatings(self):
        if not self.token:
            logging.info("No token found. Attempting login first...")
            self.login()
            if not self.token:
                logging.info("Login failed, cannot proceed to /myshows/")
                return

        logging.info(f"Using Token for /artistsSCRatings/: {self.token}")

        with self.client.get("/artistsSCRatings",  # Ensure correct API path
                             name="artistsSCRatings",
                             headers=self.headers,  # Send Authorization header
                             timeout=120,
                             catch_response=True) as response:
            logging.info(f"artistsSCRatings Response Code: {response.status_code}")
            logging.info(f"artistsSCRatings Response Body: {response.text}")

            if response.status_code in [200, 302]:
                logging.info("artistsSCRatings page loaded")
            else:
                logging.info(f"artistsSCRatings page failed with status code {response.status_code}: {response.text}")
    @task(2)
    def contact(self):
        if not self.token:
            logging.info("No token found. Attempting login first...")
            self.login()
            if not self.token:
                logging.info("Login failed, cannot proceed to /myshows/")
                return

        logging.info(f"Using Token for /contact/: {self.token}")

        with self.client.get("/contact",  # Ensure correct API path
                             name="contact",
                             headers=self.headers,  # Send Authorization header
                             timeout=120,
                             catch_response=True) as response:
            logging.info(f"contact Response Code: {response.status_code}")
            logging.info(f"contac Response Body: {response.text}")

            if response.status_code in [200, 302]:
                logging.info("contact page loaded")
            else:
                logging.info(f"contact page failed with status code {response.status_code}: {response.text}")

class UserBehaviour(HttpUser):
    wait_time = between(1, 5)
    host = "https://www.youbloomconnect.com"
    tasks = [MyTaskSet0]
