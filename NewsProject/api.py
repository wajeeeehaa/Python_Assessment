import requests
from processors import measure_time
from exceptions import NewsAPIError


# Create a function that:
# •	Sends a GET request
# •	Checks the status code
# •	Converts response to JSON
# •	Handles errors using try/except
@measure_time
def fetch_news():
    url = "https://saurav.tech/NewsAPI/top-headlines/category/technology/us.json"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise NewsAPIError(
                f"API request failed with status code {response.status_code}"
            )
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        raise NewsAPIError(f"API request failed: {e}")
    except ValueError:
        raise NewsAPIError("Invalid JSON response")
