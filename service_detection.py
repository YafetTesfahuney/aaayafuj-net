# scripts/xss_detection.py
import requests

def detect_xss(url):
    payloads = ['<script>alert(1)</script>', '<img src="x" onerror="alert(1)">']
    for payload in payloads:
        response = requests.get(url + payload)
        if payload in response.text:
            return True
    return False
