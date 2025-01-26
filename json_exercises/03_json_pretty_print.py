import json

sample_json = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(json.dumps(sample_json, indent=2, separators=(",", "= ")))
