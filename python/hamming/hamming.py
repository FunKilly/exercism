def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands don't have same length")
    try:
        return sum(1 for s1,s2 in zip(strand_a,strand_b) if s1 != s2)
    except Exception:
        raise Exception("Exception ble ble")


