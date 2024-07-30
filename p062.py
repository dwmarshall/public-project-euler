from collections import defaultdict
from itertools import count

D = 5

cube_dict = defaultdict(list)

for n in count(1):
    cube = n * n * n
    form = "".join(sorted(str(cube)))
    cube_dict[form].append(cube)
    if len(cube_dict[form]) == D:
        print(min(cube_dict[form]))
        break
