import requests
from utils.config import BASE_URL, MGMT_KEY, CLIENT_KEY

class FormbricksAPI:
    def __init__(self):
        self.mgmt_headers = {
            "Authorization": f"Bearer {MGMT_KEY}",
            "Content-Type": "application/json"
        }
        self.client_headers = {
            "Authorization": f"Bearer {CLIENT_KEY}",
            "Content-Type": "application/json"
        }

    def create_user(self, user):
        return requests.post(
            f"{BASE_URL}/api/management/users",
            json=user,
            headers=self.mgmt_headers
        ).json()

    def create_survey(self, survey):
        return requests.post(
            f"{BASE_URL}/api/management/surveys",
            json=survey,
            headers=self.mgmt_headers
        ).json()

    def submit_response(self, survey_id, response):
        return requests.post(
            f"{BASE_URL}/api/client/surveys/{survey_id}/responses",
            json=response,
            headers=self.client_headers
        ).json()
