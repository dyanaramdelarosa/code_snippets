import json

sample_json = """{"key1": "value1", "key2": "value2"}"""
input_data = json.loads(sample_json)
print(input_data["key2"])
