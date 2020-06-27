# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateTransitionAPITestCase::test_case status'] = 200

snapshots['TestCase01CreateTransitionAPITestCase::test_case body'] = {
    'description': 'string',
    'from_state': {
        'from_state_id': 1,
        'name': 'string'
    },
    'name': 'string',
    'to_state': {
        'name': 'string',
        'to_state_id': 1
    },
    'transition_id': 1
}

snapshots['TestCase01CreateTransitionAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '152',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
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

snapshots['TestCase01CreateTransitionAPITestCase::test_case name'] = 'transition_0'

snapshots['TestCase01CreateTransitionAPITestCase::test_case description'] = 'description_0'

snapshots['TestCase01CreateTransitionAPITestCase::test_case from_state'] = GenericRepr('<State: State object (1)>')

snapshots['TestCase01CreateTransitionAPITestCase::test_case to_state'] = GenericRepr('<State: State object (2)>')
