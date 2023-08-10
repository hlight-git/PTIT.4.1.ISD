import json
import requests
def predict(t, h, ws):
    url = 'http://127.0.0.1:5000/iot/weather/forecast'
    data = {"temperature":t, "humidity":h, "wind_speed":ws}
    data_json = json.dumps(data)
    print(data_json)
    headers = {'Content-type':'application/json'}
    response = requests.post(url, data=data_json, headers=headers)
    result = json.loads(response.text)
    return result
if __name__ == "__main__":
    predictions = predict(25.6, 45.1, 50.2)
    print("Rain" if predictions["prediction"] == 1 else "No rain")