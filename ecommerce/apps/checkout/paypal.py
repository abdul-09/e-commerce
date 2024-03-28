import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AQnuIBp5uWddzk8kAUt10mmPCP9NpmPbJ4ggP0JzQlry6Y77iCMKdm9bxP5ELGjE6qBhGA0H7JyZt_dQ"
        self.client_secret = "ELlBJuItx4d_07aBd0ataAjdMMJgMydmkH8QogoLOMcIPeDIiVn4kUZ3Kzul2pM17-nLymRdzOY3PZ6f"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
