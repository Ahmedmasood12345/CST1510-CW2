def parse_line(raw_line):
    """Parse a raw cybersecurity log line into a structured dictionary."""
    line = raw_line.strip().lower()
    parts = line.split(",")

    data = {}
    for piece in parts:
        k, v = piece.split("=")
        key = k.strip()
        val = v.strip()

        # Convert numeric values to float, keep string values as they are
        try:
            data[key] = float(val)
        except ValueError:
            data[key] = val

    return data


# Test with at least 5 raw lines varying in spacing and case
test_lines = [
    " SRC=10.0.0.5 , ATTEMPTS=12 , RESULT=FAILED ",
    "src=192.168.1.50, attempts=3, result=success",
    "   SRC=172.16.0.22 ,   ATTEMPTS=8  , RESULT=failed   ",
    "src=10.0.0.99,attempts=15,result=FAILED",
    " SRC=8.8.8.8 , attempts=1 , RESULT=success ",
]

for raw in test_lines:
    print(parse_line(raw))