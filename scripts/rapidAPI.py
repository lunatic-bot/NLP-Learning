import requests

url = "https://covid-19-data.p.rapidapi.com/country/code"

querystring = {"format":"json","code":"it"}

headers = {
	"x-rapidapi-key": "fe1ed68235msh32a574b6f4b40b4p1f1dc4jsn36910df8d279",
	"x-rapidapi-host": "covid-19-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())