import time
import random


def send_upi_payment(upi_id, amount):

    print("Processing payment...")

    time.sleep(2)

    txn = "TXN" + str(random.randint(100000, 999999))

    return {
        "status": "SUCCESS",
        "transaction_id": txn,
        "upi_id": upi_id,
        "amount": amount
    }