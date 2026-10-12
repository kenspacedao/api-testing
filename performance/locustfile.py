from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    # Wait between 1 and 2 seconds between each task per user
    wait_time = between(1, 2)

    @task(3)
    def view_posts(self):
        # task weight (3) means users perform this 3x more often
        self.client.get("/posts")

    @task(1)
    def view_single_post(self):
        self.client.get("/posts/1")
