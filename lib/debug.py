#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from department import Department

import ipdb

Department.drop_table()
Department.create_table()

ipdb.set_trace()