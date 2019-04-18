import domain_utils as du
import alexa_utils as au
import os
import json

DATA_DIR = os.path.expanduser('/home/think/Desktop/XXX')


def sample_top_1m():
    return au.sample_top_sites(
        location=DATA_DIR,
        include_rank=True,
        slices=[(10000, 0, 10000)]
    )


ALEXA_TOP1M = sample_top_1m()
ALEXA_TOP1M_URL = [x[1] for x in ALEXA_TOP1M]
print(ALEXA_TOP1M_URL[0])

LINKS = []
num = 0
fin = open("/home/think/Desktop/XXX/internal_links_1mSS.json", 'r')
data = json.loads(fin.read())
for j in data:
    print(j[1])
    for k in j[1]:
        num += 1
        if du.get_ps_plus_1(k) in ALEXA_TOP1M_URL:
            continue
        else:
            LINKS.append(k)
print(num)
print(len(LINKS))
with open("ALL_INTERNAL_LINKS_1mSS.json", 'w') as f:
    json.dump(LINKS, f)
