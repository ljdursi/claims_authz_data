package static

test_valid_allowed {
    allow with input as { "path": ["individuals", "P001"],
                          "user": "alice",
                          "method": "GET",
                          "token": {"payload":{"researcher":true, "entitlements": ["primary"]}} }
}

test_notaresearcher_unallowed {
    not allow with input as { "path": ["individuals", "P001"],
                              "user": "bob",
                              "method": "GET",
                              "token": {"payload":{"researcher":false, "entitlements": ["primary", "secondaryA"]}} }
}

test_noentitlements_unallowed {
    not allow with input as { "path": ["individuals", "P001"],
                              "user": "frank",
                              "method": "GET",
                              "token": {"payload":{"researcher":true, "entitlements": []}} }
}
