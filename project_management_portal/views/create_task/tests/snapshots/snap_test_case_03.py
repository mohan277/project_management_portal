# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateTaskAPITestCase::test_case status'] = 200

snapshots['TestCase01CreateTaskAPITestCase::test_case body'] = {
    'created_at': '2020-06-26 17:25:16',
    'created_by': 'username',
    'description': 'string',
    'issue_type': 'Task',
    'project': 'project_0',
    'state': 'state_0',
    'task_id': 2,
    'title': 'string'
}

snapshots['TestCase01CreateTaskAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '187',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin',
        'Vary'
    ],
    'x-frame-options': [
        'DENY',
        'X-Frame-Options'
    ]
}

snapshots['TestCase01CreateTaskAPITestCase::test_case title'] = 'string'

snapshots['TestCase01CreateTaskAPITestCase::test_case description'] = 'string'

snapshots['TestCase01CreateTaskAPITestCase::test_case project'] = 1

snapshots['TestCase01CreateTaskAPITestCase::test_case state'] = 1

snapshots['TestCase01CreateTaskAPITestCase::test_case created_by'] = 1
