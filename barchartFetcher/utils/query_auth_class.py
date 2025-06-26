import httpx
import urllib.parse


class QueryAuthClass:

    def __init__(self):
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " "AppleWebKit/537.36 (KHTML, like Gecko) " "Chrome/115.0.0.0 Safari/537.36"
            )
        }
        self.cookies = self.get_cookies()
        self.XSRFToken = urllib.parse.unquote(self.cookies["XSRF-TOKEN"])
        self.headers["x-xsrf-token"] = self.XSRFToken

    def get_cookies(self):
        response = httpx.get(
            "https://www.barchart.com/stocks/quotes/AAPL/overview",
            headers=self.headers,
        )
        cookies = response.cookies
        return cookies
