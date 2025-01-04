import requests

url = "http://127.0.0.1:5000/predict"
data = {"home_team_form": 0.8, "away_team_form": 0.5, "home_score": 2, "away_score": 1}
response = requests.post(url, json=data)
print(response.json())