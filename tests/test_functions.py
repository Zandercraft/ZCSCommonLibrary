from zcscommonlib import functions


def test_great_circle():
    # Check if the distance between the specific coordinates match the answer which is already known.
    assert functions.great_circle(52.370216, 4.895168, 52.520008, 13.404954) == 947546.2822650459


def test_month():
    # Check that months 1 and 12 return "January" and "December".
    assert functions.month(1) == "January"
    assert functions.month(12) == "December"
