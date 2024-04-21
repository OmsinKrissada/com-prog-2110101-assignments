def read_data():
    dat = []
    R = int(input())
    for r in range(R):
        dat.append([int(e) for e in input().strip().split()])
    return dat

def check_around():
    pass

def count_peak(data):
    peaks = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            if data[i][j] > data[i-1][j] and \
               data[i][j] > data[i+1][j] and \
               data[i][j] > data[i][j-1] and \
               data[i][j] > data[i][j+1]:
                peaks += 1
    return peaks

exec(input().strip())
