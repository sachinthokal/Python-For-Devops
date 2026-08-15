# if/elif/else and for/while loops.

def deploy_advice(env):
    if env == "prd":
        return "Don't deploy on Friday!"
    elif env == "stg":
        return "Take a backup & test well."
    elif env == "test":
        return "Test it thoroughly."
    else:
        return "Safe to deploy any day."


for env in ["prd", "stg", "test", "dev"]:
    print(f"{env:5} -> {deploy_advice(env)}")

print("\nCloud providers we care about:")
clouds = ["aws", "azure", "gcp"]
for cloud in clouds:
    print(" -", cloud.upper())

print("\nRolling out in:")
seconds = 3
while seconds > 0:
    print(f"  {seconds}...")
    seconds -= 1
print("  Deployed!")
