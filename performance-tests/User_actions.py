# User class 

from locust import HttpUser, between
import youbloomconnect
import High_user_tasks
import Low_user_tasks

class UserOnHost1(HttpUser):
    wait_time = between(1, 5)
    host = "https://youbloom.com"
    
    tasks = [High_user_tasks.MyTaskSet1, Low_user_tasks.MyTaskSet]
    

class UserOnHost2(HttpUser):
    wait_time = between(1, 5)
    host = "https://youbloomconnect.com"
    
    tasks = [youbloomconnect.MyTaskSet0]