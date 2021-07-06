import requests
from requests.exceptions import HTTPError
# pip install requests
from LDAPIWrapper import checkRateLimit


API_KEY = "your-api-key"
URL = '/projects/[YOURPROJECT]/environments/[YOURENVIRONMENT]'
BODY = {}

REPEATS = 100

while REPEATS > 0:
    apiTest = checkRateLimit("GET", URL, API_KEY, BODY)
    rateLimitRemaining = apiTest.headers['X-Ratelimit-Route-Remaining']
    print('Current repeats: ' + str(REPEATS) + '. Current rate limit: ' + str(rateLimitRemaining))
    REPEATS -= 1
