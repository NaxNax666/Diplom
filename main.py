


def generate_transaction(user, weight, group, sender, recipient, number):
    global key
    transaction = {"additional": {"number": number, "time": time.time(), "weight": weight, "group": group},
                   "user": {"public_key": key[0], "address": user["address"], "post_code": user["post_code"]},
                   "content": {'sender': sender, "recipient": recipient}}
    return transaction

def sign_transaction(transaction):
    global key
    signature = rsa.sign(message=str(transaction).encode(), priv_key=key[1], hash_method='SHA-256')
    return signature