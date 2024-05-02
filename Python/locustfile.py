from locust import HttpUser, between, task

class PaymentUser(HttpUser):
    # Set a wait time between 1 and 5 seconds
    wait_time = between(5, 9)

    @task
    def visit_payment(self):
        # Simulate a GET request to /payment
        self.client.get("/payment")
    
    @task
    def post_successful_payment(self):
        # Simulate a POST request with valid data
        payment_data = {
            "amount": "100.00",
            "card_number": "1234567812345678",
            "expiry": "12/25",
            "cvv": "123"
        }
        self.client.post("/payment", data=payment_data)
    
    @task
    def post_failed_payment(self):
        # Simulate a POST request with invalid data
        payment_data = {
            "amount": "-100.00",
            "card_number": "1234567812345678",
            "expiry": "12/25",
            "cvv": "123"
        }
        self.client.post("/payment", data=payment_data)