# diagnostic.py

from functools import wraps


# Decorator
def logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        

        result = function(*args, **kwargs)

        
        return result

    return wrapper


# Generate equipment readings
@logger
def generate_readings(last_name, seed_digit, artist):
    base = len(last_name) + seed_digit + len(artist)

    readings = [
        base + 10,
        base + 15,
        base + 20,
        base + 25,
        base + 30
    ]

    return readings


# Validate readings
@logger
def validate_reading(reading):
    try:
        reading = float(reading)

        if reading < 0:
            raise ValueError("Reading cannot be negative.")

        return True

    except (ValueError, TypeError) as error:
        print("[ERROR]", error)
        return False


# Calculate average
@logger
def calculate_average(readings):
    if not readings:
        return 0

    return sum(readings) / len(readings)


# Classify equipment condition
@logger
def classify_equipment(average):
    if average >= 80:
        return "CRITICAL"

    elif average >= 60:
        return "WARNING"

    else:
        return "NORMAL"


# Main diagnostic process
def run_diagnostic(last_name, seed_digit, artist):

    print("\n===== EQUIPMENT DIAGNOSTIC SYSTEM =====")

    readings = generate_readings(
        last_name,
        seed_digit,
        artist
    )

    print("\nGenerated Equipment Data:")
    print(readings)

    valid_readings = []
    invalid_readings = []

    for reading in readings:

        if validate_reading(reading):
            valid_readings.append(reading)

        else:
            invalid_readings.append(reading)

    average = calculate_average(valid_readings)

    condition = classify_equipment(average)

    print("\nValidation Results:")
    print("Valid readings:", valid_readings)
    

    print("\nDiagnostic Results:")
    print("Average:", average)
    print("Equipment Status:", condition)

    return {
        "readings": readings,
        "valid": valid_readings,
        "invalid": invalid_readings,
        "average": average,
        "status": condition
    }