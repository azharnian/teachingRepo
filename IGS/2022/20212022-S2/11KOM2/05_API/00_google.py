import requests

response = requests.get("https://www.google.com")

"""
requests.get('url')
requests.post('url')
requests.put('url')
requests.patch('url')
requests.delete('url')
"""

print(response.text)