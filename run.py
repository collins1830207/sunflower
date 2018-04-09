#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
from web import app
from generate import Generate

if __name__ == '__main__':
    gen = Generate()
    t = time.time()
    gen()
    print("Generated!!!",time.time()-t)
    app.run()



