import os
import requests
import logging
import logging.config
import yaml

with open("logging.yaml", "rt") as f:
	logging.config.dictConfig(yaml.safe_load(f.read()))

logger = logging.getLogger("lendo-fetcher")

BASE_URL = "https://sample-database-1008463684624.europe-north1.run.app"

# Fail fast with KeyError if missing environment variables
TOKEN = os.environ["LENDO_API_TOKEN"]
DATE_FROM = os.environ["DATE_FROM"]
DATE_TO = os.environ["DATE_TO"]


def fetch(endpoint):
    params = {
        "token": TOKEN,
        "dateFrom": DATE_FROM,
        "dateTo": DATE_TO,
    }
    url = f"{BASE_URL}/{endpoint}"
    r = requests.get(url, params)
    logger.info("Fetched %s", url)
    result = r.json()
    logger.info("Number of results: %s", len(result))
    return result


def main():
    params = {
        "token": TOKEN,
        "dateFrom": DATE_FROM,
        "dateTo": DATE_TO,
    }

    applications = fetch("applications")
    responses = fetch("responses")

    responses_by_application_id = {}
    for r in responses:
        app_id = r.get('Application Id')
        responses_by_application_id.setdefault(app_id, []).append(r)

    print(responses_by_application_id.keys())
    for a in applications:
        app_id = a.get('Application Id')
        a['responses'] = responses_by_application_id.get(appid)


    with  open('result.json', 'w') as f: 
       pass 


if __name__ == "__main__":
    main()
