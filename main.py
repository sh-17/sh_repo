import requests
response = requests.get("https://api.covid19india.org/data.json")
coviddata = response.json()

for i in coviddata:
    print(i)

print(len(coviddata["cases_time_series"]))
print(coviddata["cases_time_series"][0])
print(coviddata["cases_time_series"][-1])


