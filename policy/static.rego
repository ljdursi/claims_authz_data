package static

consents = {"primary":["P001", "P002", "P003", "P004", "P005", "P006"], 
            "secondaryA":["P001", "P002", "P003"], 
            "secondaryB":["P004", "P005", "P006"]}

import input

# input = {
#   "path": ["individuals", "P001"],
#   "user": "alice",
#   "method": "GET"
#    token.payload.entitlements == ["Primary", "SecondaryA"]
#    token.payload.researcher == "True"
# }

default allow = false

# Allow users get data they're authorized for if they are researchers
allow {
  input.method = "GET"
  input.path = ["individuals", iid]
  input.token.payload.researcher == "True"
  consents[iid][_] == input.token.payload.entitlements[_]
}
