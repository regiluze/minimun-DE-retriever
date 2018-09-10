# -*- coding: utf-8 -*-

from expects import *

from server import app, BASE_PATH
from flask import json

with describe('Minimum extra DE data center REST API service acceptance specs'):
    with before.each:
        self.app = app.test_client()

    with context('test case 1'):
        with before.each:
            self.input_data = {'DM_capacity': 20,
                               'DE_capacity': 8,
                               'data_centers': [{'name': 'Paris', 'servers': 20 }, {'name': 'Stockholm', 'servers': 62}]}

        with it('returns 200 status code'):
            result = self.app.put(BASE_PATH, data=json.dumps(self.input_data), content_type='application/json')

            expect(result.status_code).to(equal(200))

        with it('returns Paris data center with 8 as minimun extra DE'):
            result = self.app.put(BASE_PATH, data=json.dumps(self.input_data), content_type='application/json')
            result = json.loads(result.data)

            expect(result['DE']).to(equal(8))
            expect(result['DM_data_center']).to(equal('Paris'))

    with context('test case 2'):
        with before.each:
            self.input_data = {'DM_capacity': 6,
                               'DE_capacity': 10,
                               'data_centers': [{'name': 'Paris', 'servers': 30 }, {'name': 'Stockholm', 'servers': 66}]}

        with it('returns 200 status code'):
            result = self.app.put(BASE_PATH, data=json.dumps(self.input_data), content_type='application/json')

            expect(result.status_code).to(equal(200))

        with it('returns Stockholm data center with 9 as minimun extra DE'):
            result = self.app.put(BASE_PATH, data=json.dumps(self.input_data), content_type='application/json')
            result = json.loads(result.data)

            expect(result['DE']).to(equal(9))
            expect(result['DM_data_center']).to(equal('Stockholm'))

    with context('test case 3'):
        with before.each:
            self.input_data = {'DM_capacity': 12,
                               'DE_capacity': 7,
                               'data_centers': [{'name': 'Berlin', 'servers': 11 }, {'name': 'Stockholm', 'servers': 21}]}

        with it('returns 200 status code'):
            result = self.app.put(BASE_PATH, data=json.dumps(self.input_data), content_type='application/json')

            expect(result.status_code).to(equal(200))

        with it('returns Berlin data center with 3 as minimun extra DE'):
            result = self.app.put(BASE_PATH, data=json.dumps(self.input_data), content_type='application/json')
            result = json.loads(result.data)

            expect(result['DE']).to(equal(3))
            expect(result['DM_data_center']).to(equal('Berlin'))
