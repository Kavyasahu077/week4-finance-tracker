def validate_amount(amount):

    try:
        amount = float(amount)

        if amount > 0:
            return True

        return False

    except:
        return False