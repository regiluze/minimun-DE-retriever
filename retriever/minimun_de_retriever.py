# -*- coding: utf-8 -*-

import math

class MinimunDevopsEngineerRetriever(object):

    def process(self, data):
        data_centers = data['data_centers']
        return {'DM_data_center' : data_centers[0]['name'],
                'DE' : self._calculate_DE_extra_needed(data_centers[0], data['DE_capacity'], data['DM_capacity'])}

    def _calculate_DE_extra_needed(self, data_center, de_capacity, dm_capacity):
        return math.ceil((data_center['servers'] - dm_capacity) / de_capacity)

