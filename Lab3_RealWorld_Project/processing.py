# processing.py

from functools import wraps


# ==========================================
# DECORATOR
# ==========================================

def monitor_process(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(f"\n[DECORATOR] Starting {function.__name__}")

        result = function(*args, **kwargs)

        print(f"[DECORATOR] Finished {function.__name__}")

        return result

    return wrapper


# ==========================================
# PROCESS TELEMETRY
# ==========================================

@monitor_process
def process_telemetry(readings):

    processed = []

    for reading in readings:

        try:

            value = float(reading)

            if value < 0:
                raise ValueError("Negative telemetry value")

            processed.append(value)

        except (ValueError, TypeError) as error:

            print("[ERROR]", error)

    return processed


# ==========================================
# LAMBDA FILTER
# ==========================================

def filter_abnormal(readings):

    abnormal = list(
        filter(
            lambda x: x >= 80,
            readings
        )
    )

    return abnormal


# ==========================================
# RECURSIVE ANALYSIS
# ==========================================

def recursive_analysis(readings, index=0):

    # BASE CONDITION
    if index >= len(readings):

        return []

    current = readings[index]

    if current >= 80:

        result = ["ABNORMAL"]

    else:

        result = ["NORMAL"]

    return result + recursive_analysis(
        readings,
        index + 1
    )


# ==========================================
# FINAL DIAGNOSTIC REPORT
# ==========================================

def diagnostic_report(readings):

    abnormal = filter_abnormal(readings)

    analysis = recursive_analysis(readings)

    return {
        "processed": len(readings),
        "valid": len(readings),
        "invalid": 0,
        "abnormal": len(abnormal),
        "analysis": analysis
    }