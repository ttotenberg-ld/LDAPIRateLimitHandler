# LDAPIRateLimitHandler

## Overview
Rate limiting is a best practice in APIs, to prevent overzealous integrations or malicious attackers from overwhelming the server with unlimited requests. You can read about the [LaunchDarkly API's rate limiting here.](https://apidocs.launchdarkly.com/reference#rate-limiting)

## What does this wrapper do?
Using this wrapper will do a few things in this order:
1. Performs your API call
1. Checks the remaining rate limit after that call
    1. Via the ['X-Ratelimit-Route-Remaining'] response header
1. Compares the remaining rate limit against a threshold
1. If the threshold is high enough, it returns the API response
1. If the remaining rate limit is below the threshold, it does the following:
    1. Gets the time of the next rate limit reset via the ['X-Ratelimit-Reset'] response header
    1. Sleeps until that rate limit reset time
    1. Retries your function at that time (step 1)
    1. Will continue to retry for X times (5 by default) before giving up and returning an error
    
## Usage
Look at [example.py](/Example.py) for a sample call.

This wrapper takes four parameters in `LDAPIWrapper.checkRateLimit`, in the [requests library](https://docs.python-requests.org/en/master/) format.

### method
"GET", "POST", "PATCH", "DELETE"

### url
Everything after the base API url. The base url is: `https://app.launchdarkly.com/api/v2`
Example: `'/projects/my-cool-project/environments/test'`

### apikey
Your LaunchDarkly API key as a string.
Example: `'api-12345-abcd-4321-zyxw-1a2b3c4d'`

### body
The body of your request. For a blank body, pass in `{}`

## Note
You should not blindly copy + paste this wrapper for your use. The way it is currently written, it may successfully execute your call multiple times if below the rate limit threshold. So, there's a risk of accidentally repeating actions that should not be repeated. Maybe that doesn't matter for your usage, but you should modify this wrapper in your own environment as needed.

Questions? Comments? Feedback? Hopes? Dreams? Let me know! :) Hope this helps.
