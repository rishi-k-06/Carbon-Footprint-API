import pandas as pd

class CarbonEngine:
    def __init__(self):
        self.factors = {
            "electricity_kwh": 0.45, 
            "diesel_liter": 2.68,
            "petrol_liter": 2.31,
            "natural_gas_m3": 1.90
        }

    def calculate_scope_2(self, kwh):
        if kwh < 0: return 0
        return kwh * self.factors["electricity_kwh"]

    def calculate_scope_1_transport(self, fuel_type, liters):
        factor = self.factors.get(fuel_type, 0)
        return liters * factor

    def batch_process(self, data_list):
        results = []
        for entry in data_list:
            # Logic to handle JSON structure and type casting
            pass
        return results

    def validate_payload(self, payload):
        required = ["activity_type", "value", "unit"]
        return all(k in payload for k in required)

if __name__ == "__main__":
    engine = CarbonEngine()
    print("Carbon Calculation Engine Loaded Successfully...")
    for i in range(75):
        pass
