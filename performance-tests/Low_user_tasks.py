from locust import HttpUser,SequentialTaskSet, task, tag, between
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

class MyTaskSet(SequentialTaskSet):
    def on_start(self):
        print("Starting the tasks")
    
    @task
    @tag('Homepage')
    def homepage(self):
        try:
            response = self.client.get("/")
            logging.info(f"Homepage response: {response.status_code}")
        except Exception as e:
            logging.error(f"Homepage request failed: {e}")
    
    @task
    @tag('About')
    def about(self):
        try:
            response = self.client.get("/about/")
            logging.info(f"About response: {response.status_code}")
        except Exception as e:
            logging.error(f"About request failed: {e}")
    
    @task
    @tag('Contact')
    def contact(self):
        try:
            response = self.client.get("/contact/")
            logging.info(f"Contact response: {response.status_code}")
        except Exception as e:
            logging.error(f"Contact request failed: {e}")
    
    @task
    @tag('Intern')
    def intern(self):
        try:
            response = self.client.get("/intern/")
            logging.info(f"Intern response: {response.status_code}")
        except Exception as e:
            logging.error(f"Intern request failed: {e}")
    
    @task
    @tag('Blog')
    def blog(self):
        try:
            response = self.client.get("/blog/")
            logging.info(f"Blog response: {response.status_code}")
        except Exception as e:
            logging.error(f"Blog request failed: {e}")
    
    @task
    @tag('Privacy')
    def privacy(self):
        try:
            response = self.client.get("/privacy/")
            logging.info(f"Privacy response: {response.status_code}")
        except Exception as e:
            logging.error(f"Privacy request failed: {e}")
    
    @task
    @tag('Help_Center')
    def help(self):
        try:
            response = self.client.get("/knowledge-base/")
            logging.info(f"Help Center response: {response.status_code}")
        except Exception as e:
            logging.error(f"Help Center request failed: {e}")
    
    @task
    @tag('Terms')
    def terms(self):
        try:
            response = self.client.get("/youbloom-at-bloom-2025/")
            logging.info(f"Terms response: {response.status_code}")
        except Exception as e:
            logging.error(f"Terms request failed: {e}")
            
    @task
    @tag('Signup')
    def signup(self):
        # Get request 
        try:
            response = self.client.get("/become-a-show-creator/")
            logging.info(f"Signup response: {response.status_code}")
        except Exception as e:
            logging.error(f"Signup request failed: {e}")
            
    def on_stop(self):
        print("Stopping the tasks")
