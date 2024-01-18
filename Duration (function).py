def str2hms(hms_str):
    t = hms_str.split(':')
    return int(t[0]),int(t[1]),int(t[2])
def hms2str(h,m,s):
    return ('0'+str(h))[-2:] + ':' + \
    ('0'+str(m))[-2:] + ':' + \
    ('0'+str(s))[-2:]

def to_sec(h,m,s):
    return h*60*60 + m*60 + s
    
def to_hms(total):
    h = total // 60 // 60
    m = total // 60 % 60
    s = total % 60
    return h, m, s

def diff(h1,m1,s1,h2,m2,s2):
    return to_hms(to_sec(h2, m2, s2) - to_sec(h1, m1, s1))

def main():
 hms_start = input()
 hms_end = input()
 l_tup = str2hms(hms_start)
 r_tup = str2hms(hms_end)
 diff_val = diff(l_tup[0], l_tup[1], l_tup[2], r_tup[0], r_tup[1], r_tup[2])
 print(hms2str(diff_val[0], diff_val[1], diff_val[2]))

exec(input())
