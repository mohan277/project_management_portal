# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01ListOfTasksAPITestCase::test_case status'] = 200

snapshots['TestCase01ListOfTasksAPITestCase::test_case body'] = {
    'tasks': [
        {
            'created_at': '2020-06-26 20:57:25',
            'created_by': '',
            'description': 'description_0',
            'issue_type': 'Task',
            'project': 'project_0',
            'state': 'state_0',
            'task_id': 1,
            'title': 'title_0'
        },
        {
            'created_at': '2020-06-26 20:57:25',
            'created_by': '',
            'description': 'description_1',
            'issue_type': 'Bug',
            'project': 'project_0',
            'state': 'state_0',
            'task_id': 2,
            'title': 'title_1'
        },
        {
            'created_at': '2020-06-26 20:57:25',
            'created_by': '',
            'description': 'description_2',
            'issue_type': 'Developer story',
            'project': 'project_0',
            'state': 'state_0',
            'task_id': 3,
            'title': 'title_2'
        },
        {
            'created_at': '2020-06-26 20:57:25',
            'created_by': '',
            'description': 'description_3',
            'issue_type': 'User story',
            'project': 'project_0',
            'state': 'state_0',
            'task_id': 4,
            'title': 'title_3'
        },
        {
            'created_at': '2020-06-26 20:57:25',
            'created_by': '',
            'description': 'description_4',
            'issue_type': 'Enhancement',
            'project': 'project_0',
            'state': 'state_0',
            'task_id': 5,
            'title': 'title_4'
        }
    ],
    'total_count_of_tasks': 5
}

snapshots['TestCase01ListOfTasksAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '1006',
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
