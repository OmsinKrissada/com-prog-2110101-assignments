def get_acgt_count(data):
    return [data.count(c) for c in 'ACGT']
    # ver. without using count() :)
    # 
    # counts = [0, 0, 0, 0]
    # for c in data:
    #     for i, g in enumerate('ACGT'):
    #         if c == g:
    #             counts[i] += 1
    # return counts

def get_ag_ct_ratio(data):
    counts = get_acgt_count(data)
    upper = counts[0] + counts[2]
    lower = counts[1] + counts[3]
    return upper / lower if lower != 0 else -1.0
    
def get_gc_percentage(data):
    counts = get_acgt_count(data)
    interested = counts[1] + counts[2]
    return interested / len(data)

# def get_repeat_count(data, pattern):
#     # big fail :(
#     # 
#     # found = pattern_lookup_index = 0
#     # for c in data:
#     #     if c != pattern[pattern_lookup_index]:
#     #         if found > 0:
#     #             break
#     #         else:
#     #             continue
#     #     if pattern_lookup_index == len(pattern) - 1:
#     #         found += 1
#     #         pattern_lookup_index = 0
#     #         continue
#     #     pattern_lookup_index += 1
#     # return found if found > 1 else 0
#     pattern_repeat = 1
#     while True:
#         if pattern * pattern_repeat not in data:
#             return pattern_repeat - 1 if pattern_repeat - 1 > 1 else 0
#         pattern_repeat += 1

# def get_repeat_count(data, pattern):
#     count = 0
#     for i in range(len(data)-2):
#         if data[i+1] == pattern[1] and data[i] == pattern[0]:
#             count += 1
#         elif data[i] != data[i+2] and data[i-1] != data[i+1]:
#             if count > 1:
#                 break
#             else:
#                 count = 0
#     return count

# def get_repeat_count(data, pattern):
#     count = 0
#     for i in range(len(data)-1):
#         if data[i+1] == pattern[1] and data[i] == pattern[0]:
#             count += 1
#         if i < len(data)-2 and data[i] != data[i+2] and data[i-1] != data[i+1]:
#             if count > 1:
#                 break
#             else:
#                 count = 0
#     return count

def get_repeat_count(data, pattern):
    count = 0
    for i in range(len(data)-1):
        if data[i+1] == pattern[1] and data[i] == pattern[0]:
            count += 1
        elif i < len(data) - 2 and data[i] != pattern[0] and data[i] != data[i+2]  and data[i-1] != pattern[1]:
            if count == 1:
                count = 0
            elif count > 1:
                break
    if count == 1:
        count = 0
    return count

# def get_acgt_count(data):
#   date_A=0mm
#   date_C=0
#   date_G =0
#   date_T=0
#   for a in data:
#     if 'A'==a:
#       date_A+=1
#     if 'C'==a:
#       date_C+=1
#     if 'G'==a:
#       date_G+=1
#     if 'T'==a:
#       date_T+=1
#   return [date_A,date_C,date_G,date_T]

# def get_ag_ct_ratio(data):
#   n_data=get_acgt_count(data)
#   if int(n_data[1])+int(n_data[3])==0:
#     return -1.0
#   else:
#     return (float(n_data[0])+float(n_data[2]))/(float(n_data[1]+float(n_data[3])))

# def get_gc_percentage(data):
#   n_data=get_acgt_count(data)
#   return (float(n_data[1])+float(n_data[2]))/len(data)

# def get_repeat_count(data, pattern):
#   if pattern*2 in data:
#     n=2
#     while pattern*n in data:
#       n+=1
#     else:
#       return n-1
#   else:
#     return 0




import copy
def test_f(case_name, f_name, expected, f_kwargs, allowed_unsorted_result=False):
    def show_warning(case_name, str1, str2, expected, actual):
        print("WARNING!! Something went wrong at", case_name)
        warning_txt = " ".join([str(e) for e in [str1, str2, expected, "instead of", actual]])
        if len(warning_txt) < 100:
            print(warning_txt)
        else:
            print(str1)
            print(str2)
            print(expected)
            print("instead of")
            print(actual)

    f = eval(f_name)
    mut_val_b4_test = {}
    for key, val in f_kwargs.items():
        if type(val) is list:
            mut_val_b4_test[key] = copy.deepcopy(val)
    call_txt = f_name + "(" + str(list(f_kwargs.values()))[1:-1] + ")"
    result = f(**f_kwargs)
    if allowed_unsorted_result:
        if type(result) is list:
            result.sort()
            expected.sort()
    for key in mut_val_b4_test:
        if mut_val_b4_test[key] != f_kwargs[key]:
            show_warning(case_name,
                         "After calling " + call_txt + ",",
                         "argument " + key + " must have its value as before:",
                         mut_val_b4_test[key],
                         f_kwargs[key])
            return 1
    if type(expected) is not type(result):
        show_warning(case_name, call_txt, "should return variable type", type(expected), type(result))
        return 1
    if result != expected:
        show_warning(case_name, call_txt, "should return", expected, result)
        return 1
    return 0

def run_test(f_name, test_cases):
    print("------------------------------------------------------------")
    err_code = 0
    for idx, test_kwargs in enumerate(test_cases):
        case_name = "test " + f_name + " #" + str(idx+1)
        err_code |= test_f(case_name, f_name, **test_kwargs)
    if not err_code:
        print("Your function " + f_name + " is working well so far")

def test_get_acgt_count():
    test_cases = []
    test_cases.append({"f_kwargs": {"data": "TCCGATT"},
                       "expected": [1, 2, 1, 3]})
    test_cases.append({"f_kwargs": {"data": "AAGAA"},
                       "expected": [4, 0, 1, 0]})
    run_test("get_acgt_count", test_cases)

def test_get_ag_ct_ratio():
    test_cases = []
    test_cases.append({"f_kwargs": {"data": "TCCGATT"},
                       "expected": 0.4})
    test_cases.append({"f_kwargs": {"data": "AAGAA"},
                       "expected": -1.0})
    run_test("get_ag_ct_ratio", test_cases)

def test_get_gc_percentage():
    test_cases = []
    test_cases.append({"f_kwargs": {"data": "TCCGATT"},
                       "expected": 3/7})
    test_cases.append({"f_kwargs": {"data": "AAGAA"},
                       "expected": 1/5})
    run_test("get_gc_percentage", test_cases)

def test_get_repeat_count():
    test_cases = []
    test_cases.append({"f_kwargs": {"data": "TGACACACGG", "pattern": "AC"},
                       "expected": 3})
    test_cases.append({"f_kwargs": {"data": "ACAC", "pattern": "AC"},
                       "expected": 2})
    test_cases.append({"f_kwargs": {"data": "CACACACA", "pattern": "AC"},
                       "expected": 3})
    test_cases.append({"f_kwargs": {"data": "GACTACCAC", "pattern": "AC"},
                       "expected": 0})
    test_cases.append({"f_kwargs": {"data": "GACTACACCAC", "pattern": "AC"},
                       "expected": 2})
    test_cases.append({"f_kwargs": {"data": "GACTACACCAC", "pattern": "AC"},
                       "expected": 2})
    test_cases.append({"f_kwargs": {"data": "ACTTACAC", "pattern": "AC"},
                       "expected": 2})
    test_cases.append({"f_kwargs": {"data": "AT_GC_AT_GC_ATATATAT_GC_AT_GC_AT".replace('_',''), "pattern": "AT"},
                       "expected": 4})
    run_test("get_repeat_count", test_cases)

test_get_acgt_count()
test_get_ag_ct_ratio()
test_get_gc_percentage()
test_get_repeat_count()