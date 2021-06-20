import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'satisfaction':0.10, 'evaluation':0.9 ,'number_of_projects':4,'average_montly_hours':200,'time_spend_company':4,'work_accident':0,'promotion':0})

print(r.json())

