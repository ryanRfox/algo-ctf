import subprocess
import json
from algokit_utils import TestNetDispenserApiClient

# create a token for dispenser login
subprocess.run(["algokit", "dispenser", "login", "--ci", "--output", "file", "--file", ".env_token"])

with open(".env_token", "r") as f:
    my_auth_token = f.readline().strip()

with open('.env_account', 'r') as env_account:
    account_data = json.load(env_account)
    receiver_address = account_data["address"]
    print(receiver_address)

# create a client to the dispenser
client = TestNetDispenserApiClient(auth_token=my_auth_token)

# check the limit
response = client.get_limit(address="receiver_address")
print(response)

# fund the account
response = client.fund(address=receiver_address, amount=1000000, asset_id=0)
print(response)
