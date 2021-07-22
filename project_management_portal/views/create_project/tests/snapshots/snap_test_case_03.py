# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03CreateProjectAPITestCase::test_case status'] = 200

snapshots['TestCase03CreateProjectAPITestCase::test_case body'] = {
    'created_at': '2020-07-02 14:35:42',
    'created_by_id': 1,
    'description': 'string',
    'developers': [
    ],
    'name': 'string',
    'project_id': 2,
    'project_type': 'Classic Software',
    'workflow_type': 'workflow_type_0'
}

snapshots['TestCase03CreateProjectAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '207',
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

snapshots['TestCase03CreateProjectAPITestCase::test_case name'] = 'string'

snapshots['TestCase03CreateProjectAPITestCase::test_case description'] = 'string'

snapshots['TestCase03CreateProjectAPITestCase::test_case workflow_type'] = 1

snapshots['TestCase03CreateProjectAPITestCase::test_case project_type'] = 'Classic Software'
