def check_rental_balance(balance, requested):
    if requested <= 0 or requested > balance:
        return False
    return True