
def minMeetingRooms(intervals):
    if not intervals:
        return 0

    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)

    # print(starts)
    # print(ends)    

    rooms = 0
    max_rooms = 0
    i,j = 0, 0

    while i< len(intervals):
        if starts[i] < ends[j]:
            rooms += 1
            max_rooms = max(rooms, max_rooms)
            i += 1
        else:
            rooms -= 1
            j += 1
    return max_rooms            


print(minMeetingRooms([[0,30],[5,10],[15,20]]))
