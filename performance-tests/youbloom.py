from locust import HttpUser, TaskSet, task, tag, constant
import logging
from faker import Faker
import json
import random
from shared import shared_file
from Low_user_tasks import MyTaskSet# Import save_user function properly

# Set up logging
logging.basicConfig(level=logging.DEBUG)


class MyTaskSet1(TaskSet):
    def on_start(self):
        """Set up headers for all requests."""
        self.headers = {"Content-Type": "application/json"}
        self.shared_file = shared_file()  # Create an instance of SharedFile

    @task(3)
    @tag('Signup')
    def signup(self):
        """Send a POST request to the signup endpoint."""
        faker = Faker()
        data = {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "email": faker.email(),
            "password": "Test@1111",
            "confirm_password": "Test@1111"
        }

        try:
            response = self.client.post(
                "/become-a-show-creator/",
                data=json.dumps(data),
                headers=self.headers,
                name="Signup",
                timeout=120  # Increased timeout
            )

            if response.status_code == 200:
                logging.info(f"Signup response: {response.status_code}")
                self.shared_file.save_user(data)  # Call the method on the instance

                # Inspect cookies set by the server (if any)
                logging.info(f"Cookies after signup: {self.client.cookies}")
            else:
                logging.error(f"Signup request failed: {response.status_code}")
                logging.error(f"Response content: {response.text}")
        except Exception as e:
            logging.error(f"Signup request failed: {e}")

    @task(2)  # Increased weight to ensure this runs more frequently
    def enter_nested_task_set2(self):
        logging.info("Switching to MyTaskset2 (Login TaskSet)")
        self.schedule_task(MyTaskset2)  # Call the class, not a method


class MyTaskset2(TaskSet):
    @task(3)
    @tag('login')
    def login(self):
        """Send a POST request to the login endpoint."""
        self.headers = {"Content-Type": "application/json"}
        logging.info("Starting MyTaskset2 (Login TaskSet)")
        try:
            with open("users.json", "r") as file:
                users = json.load(file)

            if not users:
                logging.error("No users found in the file")
                return

        except (FileNotFoundError, json.JSONDecodeError):
            logging.error("No users found")
            return

        # Select one random user
        user = random.choice(users)
        login_data = {
            "email": user["email"],
            "password": user["password"]
        }
        try:
            response = self.client.post(
                "/login/",
                data=json.dumps(login_data),
                headers=self.headers,
                name="Login",
                timeout=120  # Increased timeout
            )
            if response.status_code == 200:
                logging.info("Login successful")

                # Inspect cookies set by the server (if any)
                logging.info(f"Cookies after login: {self.client.cookies}")
            else:
                logging.error(f"Login request failed: {response.status_code}")
                logging.error(f"Response content: {response.text}")
        except Exception as e:
            logging.error(f"Login request failed: {e}")

    @task(2)  # Task to switch to MyTaskSet3 (Forgot Password)
    def enter_nested_forgot_password(self):
        logging.info("Switching to MyTaskSet3 (Forgot Password TaskSet)")
        self.schedule_task(MyTaskSet3)

    @task(1)
    def stop_nested_1(self):
        print("Stopping nested TaskSet2")
        self.interrupt()  # Exit back to parent TaskSet


class MyTaskSet3(TaskSet):
    @task(3)
    @tag('forgot_password')
    def forgot_password(self):
        """Send a POST request to the forgot password endpoint."""
        self.headers = {"Content-Type": "application/json"}
        logging.info("Starting MyTaskSet3 (Forgot Password TaskSet)")
        try:
            with open("users.json", "r") as file:
                users = json.load(file)

            if not users:
                logging.error("No users found in the file")
                return

        except (FileNotFoundError, json.JSONDecodeError):
            logging.error("No users found")
            return

        # Select one random user
        user = random.choice(users)
        login_data = {
            "email": user["email"]
        }

        try:
            # Add cookies to the request (if needed)
            cookies = {"custom_cookie": "12345"}  # Example custom cookie
            with self.client.post(
                "/login/?action=forgot_password/",
                data=json.dumps(login_data),
                headers=self.headers,
                cookies=cookies,  # Add cookies to the request
                name="forgot password",
                timeout=120
            ) as response:
                if response.status_code == 200:
                    logging.info("Forgot password successful")
                else:
                    response.failure(f"Forgot password request failed: {response.status_code}")
                    logging.error(f"Response content: {response.text}")
        except Exception as e:
            logging.error(f"Forgot password request failed: {e}")

    @task(1)  # Lower weight to ensure this runs less frequently
    def exit_nested_taskset(self):
        """Exit the nested TaskSet."""
        logging.info("Exiting MyTaskSet3 (Forgot Password TaskSet)")
        self.interrupt()  # Exit back to the parent TaskSet

    def on_stop(self):
        print("Stopping the tasks")


class UserBehaviour(HttpUser):
    wait_time = constant(4)
    host = "https://www.youbloom.com"
    tasks = [MyTaskSet1, MyTaskSet]  # Use a list for tasks