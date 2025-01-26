import json

sample_json = {"id": 1, "name": "value2", "age": 29}
with open("sorted_json.txt", mode="w") as fp:
    json.dump(sample_json, fp, sort_keys=True, indent=2, separators=(",", ": "))