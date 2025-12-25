import json
from utils.api import FormbricksAPI

def seed():
    print("🌱 Seeding Formbricks via APIs only...")

    api = FormbricksAPI()

    users = json.load(open("data/users.json"))
    surveys = json.load(open("data/surveys.json"))
    responses = json.load(open("data/responses.json"))

    created_surveys = []

    for user in users:
        api.create_user(user)

    for survey in surveys:
        created = api.create_survey(survey)
        created_surveys.append(created["id"])

    for survey_id, response in zip(created_surveys, responses):
        api.submit_response(survey_id, response)

    print("✅ Seeding complete — instance looks alive 🔥")
