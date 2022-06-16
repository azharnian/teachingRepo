import requests

def main():
	response = requests.get("http://data.fixer.io/api/latest?access_key=6777ee9c18724e5e11a54d99ffca2e44")

	if response.status_code != 200:
		raise Exception("Error ... API request unsuccessful.")

	print(response.json())

main()