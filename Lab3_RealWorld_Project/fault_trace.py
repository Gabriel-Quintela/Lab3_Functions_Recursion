# fault_trace.py

recursive_calls = 0
fault_trace = []


def generate_fault_code(last_name, seed_digit, artist):
    """
    Generate a student-specific numeric fault code.
    """

    name_value = sum(ord(char) for char in last_name)

    artist_value = sum(ord(char) for char in artist)

    fault_code = (
        name_value +
        artist_value +
        seed_digit
    )

    return fault_code


def trace_fault(code):
    global recursive_calls

    recursive_calls += 1

    fault_trace.append(code)

    print(f"Recursive call {recursive_calls}: Fault code = {code}")

    # BASE CONDITION
    if code <= 10:
        print("Base condition reached.")
        return code

    # Recursive call
    next_code = code // 2

    return trace_fault(next_code)


def run_fault_trace(last_name, seed_digit, artist):

    global recursive_calls
    global fault_trace

    recursive_calls = 0
    fault_trace = []

    print("\n===== RECURSIVE FAULT TRACE =====")

    fault_code = generate_fault_code(
        last_name,
        seed_digit,
        artist
    )

    print("Generated Fault Code:", fault_code)

    final_result = trace_fault(fault_code)

    print("\nComplete Fault Trace:")
    print(fault_trace)

    print("\nNumber of Recursive Calls:")
    print(recursive_calls)

    print("\nFinal Result:")
    print(final_result)

    return {
        "fault_code": fault_code,
        "trace": fault_trace,
        "calls": recursive_calls,
        "result": final_result
    }