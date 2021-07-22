# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_mything test_mything'] = 2

snapshots['test_int_add int_add'] = 200

snapshots['test_int_mul int_mul'] = 10000

snapshots['test_float_add float_add'] = 22.2
