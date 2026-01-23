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
payload = {
            "login":"admin",
            "password":"pass",
            "form":"submit"
    }

# Deploy the payload to the target
p = requests.post(target, data=payload, headers=headers)
print(p.status_code)

# Throws an error if credentials are invalid
if "Invalid credentials" in p.text:
    print("Bad SQL Injection")


"""
    Things I've learned:
       1. How to use the requests library to carry out an SQL injection
       2. Exactly how many headers a webpage has
"""
