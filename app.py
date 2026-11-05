def vehicle_rental(balance, days):
    if days <= 0:
        return "Invalid rental days"
    if days > balance:
        return "Insufficient rental balance"
    return "rental days approved"


if __name__ == "__main__":
    balance = int(input("Enter rental days: "))
    days= int(input("Enter rental days requested: "))
    print(request_leave(balance, days))