import lichess.api
import json

user = lichess.api.user('thibault')
with open("test_api.json", "w") as jf:
    json.dump(user, jf)

