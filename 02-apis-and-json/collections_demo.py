# list, dict and set - the collections you'll use all the time.

clouds = ["aws", "azure", "gcp"]
clouds.append("ibm")
print("clouds        :", clouds)
print("first / last  :", clouds[0], "/", clouds[-1])
print("length        :", len(clouds))

for cloud in clouds:
    marker = "(market leader)" if cloud == "aws" else ""
    print(f"  - {cloud} {marker}".rstrip())

info = {
    "name": "Shubham",
    "city": "Pune",
    "favourites": ["teaching", "movies"],
}
print("\ncity          :", info["city"])
# .get() returns a default instead of crashing when a key is missing.
print("favourites    :", info.get("favourites", "Not Found"))
print("missing key   :", info.get("hobbies", "Not Found"))

info.update({"channel": "TrainWithShubham"})
for key, value in info.items():
    print(f"  {key}: {value}")

nums = [1, 1, 2, 2, 3, 3, 4]
unique = sorted(set(nums))
print("\nunique nums   :", unique)
