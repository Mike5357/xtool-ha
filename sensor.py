import requests
from homeassistant.components.sensor import SensorEntity

URL = "http://192.168.1.78:8080/status"

class XToolF1Sensor(SensorEntity):
    def __init__(self):
        self._state = None

    @property
    def name(self):
        return "xTool F1 Status"

    @property
    def state(self):
        return self._state

    def update(self):
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            self._state = data.get("mode", "unknown")
