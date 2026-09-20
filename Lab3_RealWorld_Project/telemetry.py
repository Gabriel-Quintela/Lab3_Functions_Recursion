# telemetry.py

def telemetry_generator(last_name, seed_digit, artist):
    """
    Generator that produces telemetry readings
    without storing the entire stream.
    """

    base = len(last_name) + seed_digit + len(artist)

    for i in range(1, 11):

        temperature = base + (i * 5)

        yield temperature