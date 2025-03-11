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


def main():
    endpoints = ["applications", "responses"]
    params = {
        "token": TOKEN,
        "dateFrom": DATE_FROM,
        "dateTo": DATE_TO,
    }



    for ep in endpoints:
        url = f"{BASE_URL}/{ep}"
        r = requests.get(f"{BASE_URL}/applications", params)
        logger.info("Fetched %s", url)
        result = r.json()
        logger.info("Number of results: %s", len(result))
        # print(r.json())


if __name__ == "__main__":
    main()
