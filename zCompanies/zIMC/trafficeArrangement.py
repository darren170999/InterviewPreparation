def change_data(data, already, path):
    arrival, idx = data.pop(0)
    if arrival in already:
        while True:
            arrival += 1
            if arrival not in already:
                break
    return path, arrival, idx


def getResult(arrival, street):
    mapping = {0: [], 1: []}

    for i in range(len(arrival)):
        mapping[street[i]].append((arrival[i], i))

    prev_path = prev_arrival = None
    answer = [-1] * len(arrival)
    already = set()

    while len(mapping[0]) > 0 and len(mapping[1]) > 0:
        if mapping[0][0][0] == mapping[1][0][0]:
            if (
                prev_path is not None
                and prev_path == 0
                and prev_arrival + 1 == mapping[0][0][0]
            ):
                prev_path, prev_arrival, idx = change_data(mapping[0], already, 0)
                answer[idx] = prev_arrival
            else:
                prev_path, prev_arrival, idx = change_data(mapping[1], already, 1)
                answer[idx] = prev_arrival
        else:
            if (
                (
                    prev_path is not None
                    and prev_path == 0
                    and prev_arrival == mapping[0][0][0] - 1
                )
                or (
                    prev_path is not None
                    and mapping[0][0][0] < mapping[1][0][0]
                    and prev_arrival + 1 < mapping[1][0][0]
                )
                or (prev_path is None and mapping[0][0][0] < mapping[1][0][0])
            ):
                prev_path, prev_arrival, idx = change_data(mapping[0], already, 0)
                answer[idx] = prev_arrival
            else:
                prev_path, prev_arrival, idx = change_data(mapping[1], already, 1)
                answer[idx] = prev_arrival
        already.add(prev_arrival)

    while len(mapping[1]) > 0:
        prev_path, prev_arrival, idx = change_data(mapping[1], already, 1)
        answer[idx] = prev_arrival
        already.add(prev_arrival)

    while len(mapping[0]) > 0:
        prev_path, prev_arrival, idx = change_data(mapping[0], already, 0)
        answer[idx] = prev_arrival
        already.add(prev_arrival)
    return answer