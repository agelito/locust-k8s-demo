from locust import HttpUser, task, between


class EchoUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://echo-server:80"

    @task
    def get_echo(self):
        self.client.get("/")
