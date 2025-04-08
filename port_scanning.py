# scripts/sql_injection.py
import requests

def detect_sql_injection(url):
    payloads = ["' OR '1'='1", '" OR "1"="1']
    for payload in payloads:
        response = requests.get(url + payload)
        if "error" in response.text or "mysql" in response.text:
            return True
    return False
