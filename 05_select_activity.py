
def select_activity(activities):
    sorted_ac = sorted(activities,key=lambda time:time[1])
    res = list()
    res.append(activities[0])
    endTime = activities[0][1]
    for key in range(1,len(activities)):
        if sorted_ac[key][0] > endTime:
            res.append(sorted_ac[key])
            endTime = sorted_ac[key][1]
    return res


if __name__ == '__main__':
    # activities = [(1,4),(3,5),(0,6),(5,7),(3,8),(5,9),(6,10),(8,11),(8,12),(2,13),(12,14)]
    activities = [(1,4),(3,5),(6,10),(8,11),(8,12),(0,6),(5,7),(3,8),(5,9),(2,13),(12,14)]

    print(select_activity(activities))
