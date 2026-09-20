# STUDENT CONFIGURATION

LAST_NAME = "QUINTELA"
STUDENT_ID = "TUPM-26-3488"
FAVORITE_ARTIST = "BRUNO MARS"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)


print("Student:", LAST_NAME)
print("Seed Digit:", SEED_DIGIT)
print("Digit Sum:", ID_SUM)
print("Surname Length:", NAME_LENGTH)
print("Favorite Artist:", FAVORITE_ARTIST)


# ==========================================
# PART 1 - EQUIPMENT DIAGNOSTIC
# ==========================================

from diagnostic import run_diagnostic

result = run_diagnostic(
    LAST_NAME,
    SEED_DIGIT,
    FAVORITE_ARTIST
)

print("\n===== DIAGNOSTIC FINAL OUTPUT =====")
print("Equipment Status:", result["status"])
print("Average Reading:", result["average"])
print("Valid Readings:", len(result["valid"]))
print("Invalid Readings:", len(result["invalid"]))


# ==========================================
# PART 2 - RECURSIVE FAULT TRACE
# ==========================================

from fault_trace import run_fault_trace

fault_result = run_fault_trace(
    LAST_NAME,
    SEED_DIGIT,
    FAVORITE_ARTIST
)

# ==========================================
# PART 3 - INTELLIGENT MONITORING PIPELINE
# ==========================================

from telemetry import telemetry_generator

from processing import (
    process_telemetry,
    diagnostic_report
)


print("\n")
print("==========================================")
print("INTELLIGENT EQUIPMENT MONITORING PIPELINE")
print("==========================================")


# Generate telemetry
telemetry = telemetry_generator(
    LAST_NAME,
    SEED_DIGIT,
    FAVORITE_ARTIST
)


# Process generated telemetry
processed_data = process_telemetry(telemetry)


print("\nProcessed Telemetry:")
print(processed_data)


# Create report
report = diagnostic_report(processed_data)


print("\n===== FINAL DIAGNOSTIC REPORT =====")

print("Processed Readings:",
      report["processed"])

print("Valid Readings:",
      report["valid"])

print("Invalid Readings:",
      report["invalid"])

print("Detected Abnormal Conditions:",
      report["abnormal"])

print("Equipment Analysis:",
      report["analysis"])


if report["abnormal"] > 0:

    print("Overall Equipment Status: ABNORMAL")

else:

    print("Overall Equipment Status: NORMAL")