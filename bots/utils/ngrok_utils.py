# ngrok_utils.py
import requests


def fetch_ngrok_public_urls(api_url='http://localhost:4040/api/tunnels'):
    response = requests.get(api_url)
    response_data = response.json()
    public_urls = []

    for tunnel in response_data['tunnels']:
        public_url = tunnel['public_url']
        public_urls.append(public_url)

    return public_urls
