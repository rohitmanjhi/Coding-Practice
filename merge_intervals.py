def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current) 
    return merged

# Test case
intervals = [[1,3],[2,6],[8,10],[15,18]]
print("Merged:", merge_intervals(intervals))
