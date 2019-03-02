# -*- coding: utf-8 -*-
from model.groupn import Groupn
import random
import string
import os.path
import json


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 #из каких символов случайно выбираем, чтобы увеличить частоту пробелов, умножили их количество на 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Groupn(name="", header="", footer="")] + [
    Groupn(name=random_string("name", 10), header = random_string("header", 20), footer= random_string("footer", 20))
    for i in range(5)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")

with open(file, "w") as f:
    f.write(json.dumps(testdata, default= lambda x, x.__dict__))