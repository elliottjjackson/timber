import json
import requests
import re, string, timeit
import time
import os

DOMAIN_CLIENT_ID = os.getenv("DOMAIN_CLIENT_ID")
DOMAIN_CLIENT_SECRET = os.getenv("DOMAIN_CLIENT_SECRET")


def get_token() -> str:
    response = requests.post(
        "https://auth.domain.com.au/v1/connect/token",
        data={
            "client_id": DOMAIN_CLIENT_ID,
            "client_secret": DOMAIN_CLIENT_SECRET,
            "grant_type": "client_credentials",
            "scope": "api_listings_read",
            "Content-Type": "text/json",
        },
    )
    token = response.json()
    return token["access_token"]


if __name__ == "__main__":
    access_token = get_token()
    print(type(access_token))
