MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    name = str(name)
    name = name.strip()
    if age >= 18:
        print (f'{name} is allowed to drive')
    else:
        print (f'{name} is not allowed to drive')
    return

#allowed_driving("DRIVERNAME",21)