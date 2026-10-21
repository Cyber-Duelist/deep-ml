import numpy as np
from collections import Counter

def descriptive_statistics(data: list | np.ndarray) -> dict:
    arr = np.asarray(data)
    
    # Calculate basic statistics
    mean_val = float(np.mean(arr))
    median_val = float(np.median(arr))
    
    # Calculate mode (most frequent value)
    counts = Counter(arr)
    max_freq = max(counts.values())
    modes = [val for val, count in counts.items() if count == max_freq]
    mode_val = modes[0]  # First mode if tie
    
    # Population variance and standard deviation
    variance_val = float(np.var(arr))  # ddof=0 for population variance
    std_val = float(np.std(arr))
    
    # Quartiles and IQR
    q25 = float(np.percentile(arr, 25))
    q50 = float(np.percentile(arr, 50))
    q75 = float(np.percentile(arr, 75))
    iqr = float(q75 - q25)
    
    return {
        'mean': mean_val,
        'median': median_val,
        'mode': mode_val,
        'variance': variance_val,
        'standard_deviation': std_val,
        '25th_percentile': q25,
        '50th_percentile': q50,
        '75th_percentile': q75,
        'interquartile_range': iqr
    }