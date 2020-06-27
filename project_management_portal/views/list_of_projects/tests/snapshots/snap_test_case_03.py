# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01ListOfProjectsAPITestCase::test_case status'] = 200

snapshots['TestCase01ListOfProjectsAPITestCase::test_case body'] = {
    'projects': [
        {
            'created_at': '2020-06-26 20:19:06',
            'created_by': 'username',
            'description': 'description_9',
            'name': 'project_9',
            'project_id': 10,
            'project_type': 'Classic Software',
            'workflow_type': 'workflow_type_9'
        },
        {
            'created_at': '2020-06-26 20:19:06',
            'created_by': 'username',
            'description': 'description_8',
            'name': 'project_8',
            'project_id': 9,
            'project_type': 'CRM',
            'workflow_type': 'workflow_type_8'
        },
        {
            'created_at': '2020-06-26 20:19:06',
            'created_by': 'username',
            'description': 'description_7',
            'name': 'project_7',
            'project_id': 8,
            'project_type': 'Financial',
            'workflow_type': 'workflow_type_7'
        },
        {
            'created_at': '2020-06-26 20:19:06',
            'created_by': 'username',
            'description': 'description_6',
            'name': 'project_6',
            'project_id': 7,
            'project_type': 'Classic Software',
            'workflow_type': 'workflow_type_6'
        },
        {
            'created_at': '2020-06-26 20:19:06',
            'created_by': 'username',
            'description': 'description_5',
            'name': 'project_5',
            'project_id': 6,
            'project_type': 'CRM',
            'workflow_type': 'workflow_type_5'
        },
        {
            'created_at': '2020-06-26 20:19:06',
            'created_by': 'username',
            'description': 'description_4',
            'name': 'project_4',
            'project_id': 5,
            'project_type': 'Financial',
            'workflow_type': 'workflow_type_4'
        },
        {
            'created_at': '2020-06-26 20:19:06',
            'created_by': 'username',
            'description': 'description_3',
            'name': 'project_3',
            'project_id': 4,
            'project_type': 'Classic Software',
            'workflow_type': 'workflow_type_3'
        },
        {
            'created_at': '2020-06-26 20:19:06',
            'created_by': 'username',
            'description': 'description_2',
            'name': 'project_2',
            'project_id': 3,
            'project_type': 'CRM',
            'workflow_type': 'workflow_type_2'
        },
        {
            'created_at': '2020-06-26 20:19:06',
            'created_by': 'username',
            'description': 'description_1',
            'name': 'project_1',
            'project_id': 2,
            'project_type': 'Financial',
            'workflow_type': 'workflow_type_1'
        },
        {
            'created_at': '2020-06-26 20:19:06',
            'created_by': 'username',
            'description': 'description_0',
            'name': 'project_0',
            'project_id': 1,
            'project_type': 'Classic Software',
            'workflow_type': 'workflow_type_0'
        }
    ],
    'total_count_of_projects': 10
}

snapshots['TestCase01ListOfProjectsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '2056',
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
