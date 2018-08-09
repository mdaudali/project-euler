"""Prime digit replacements
"""
from utils.utils import get_list_of_primes, get_number_digits
import sys
from collections import defaultdict
# ! Idea: Get all primes ending with 1, 3 or 7

primes = get_list_of_primes(10000000)

segments = []
current_segment = [[], [], []]
size = 1
for p in primes:
    n = get_number_digits(p)
    last_digit = p % 10
    if n != size:
        segments.extend(current_segment)
        size = n
        current_segment = [[], [], []]

    if last_digit == 1:
        current_segment[1].append(p)
    elif last_digit == 3:
        current_segment[0].append(p)
    elif last_digit == 7:
        current_segment[2].append(p)

segments.extend(current_segment)
candidates = [x for x in segments if len(x) >= 8]
for segment in candidates:
    while len(segment) >= 8:
        segment_mapped = map(lambda x: x - segment[0], segment[1:])
        counter = defaultdict(int)
        container = defaultdict(list)
        for el in segment_mapped:
            s = set(str(el))
            if len(s) == 1 or (len(s) == 2 and "0" in s):  # ! Will fail on stuff like 11, 20 etc
                m = (get_number_digits(el), str(el).count("0"))
                counter[m] += 1
                container[m].append(el)
        if segment[0] == 121313:
            print(segment[0], counter)
        for k, x in counter.items():
            if x >= 7:
                #print(segment[0], container[k])
                # ! Verify
                c = container[k]
                while len(c) >= 7:
                    count = 1
                    match = [c[0]]
                    container_mapped = map(lambda x: x - c[0], c[1:])
                    for ind, el in enumerate(container_mapped):
                        s = set(str(el))
                        if len(s) == 1 or (len(s) == 2 and "0" in s):
                            count += 1
                            match.append(container[k][ind])
                    if segment[0] == 121313:
                        print(count, match)
                    if count >= 7:
                        # ! Validate
                        f = str(match[0])
                        o = str(segment[0])
                        f = f.zfill(len(o))
                        se = set()
                        for a, i in zip(f, o):
                            if a != "0":
                                se.add(i)
                        if len(se) == 1:
                            num_shift = k[0] - k[1]
                            same = get_number_digits(segment[0]) - num_shift
                            se = set()
                            se.update(list(str(segment[0])))
                            for x in match:
                                l = list(str(segment[0] + x))
                                se.intersection_update(l)
                            if len(se) == same:
                                print("FOUND", segment[0], match, k)
                                sys.exit(0)
                    c = c[1:]
        else:
            segment = segment[1:]
    print("segment completed")
