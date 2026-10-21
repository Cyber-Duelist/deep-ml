def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    if not samples:
        return []
    
    total_samples = len(samples)
    counts = {}
    for item in samples:
        counts[item] = counts.get(item, 0) + 1
        
    return [(val, counts[val] / total_samples) for val in sorted(counts.keys())]

    pass