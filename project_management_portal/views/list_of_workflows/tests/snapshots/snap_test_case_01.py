# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01ListOfWorkflowsAPITestCase::test_case status'] = 200

snapshots['TestCase01ListOfWorkflowsAPITestCase::test_case body'] = {
    'total_count_of_workflows': 10,
    'workflows': [
        {
            'name': 'workflow_type_0',
            'workflow_id': 1
        },
        {
            'name': 'workflow_type_1',
            'workflow_id': 2
        },
        {
            'name': 'workflow_type_2',
            'workflow_id': 3
        },
        {
            'name': 'workflow_type_3',
            'workflow_id': 4
        },
        {
            'name': 'workflow_type_4',
            'workflow_id': 5
        },
        {
            'name': 'workflow_type_5',
            'workflow_id': 6
        },
        {
            'name': 'workflow_type_6',
            'workflow_id': 7
        },
        {
            'name': 'workflow_type_7',
            'workflow_id': 8
        },
        {
            'name': 'workflow_type_8',
            'workflow_id': 9
        },
        {
            'name': 'workflow_type_9',
            'workflow_id': 10
        }
    ]
}

snapshots['TestCase01ListOfWorkflowsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '518',
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
