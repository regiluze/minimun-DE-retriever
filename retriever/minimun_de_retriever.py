# -*- coding: utf-8 -*-

import math

class MinimunDevopsEngineerRetriever(object):

    def process(self, DM_capacity, DE_capacity, data_centers):
        minimum_extra_DE_amount = None
        DM_best_placed_data_center = None
        for data_center in data_centers:
            total_DE_extra_amount = self._calculate_extra_DE_needed_when_DM_place_in_current_data_center(data_centers, data_center, DE_capacity, DM_capacity)
            if self._is_needed_less_extra_DE(minimum_extra_DE_amount, total_DE_extra_amount):
                minimum_extra_DE_amount = [total_DE_extra_amount]
                DM_best_placed_data_center = [data_center]
            elif self._is_needed_the_same_extra_DE(minimum_extra_DE_amount, total_DE_extra_amount):
                minimum_extra_DE_amount.append(total_DE_extra_amount)
                DM_best_placed_data_center.append(data_center)
        DM_best_placed_data_center = sorted(DM_best_placed_data_center, key=lambda data_center: data_center['servers'], reverse=True)

        return minimum_extra_DE_amount[0], DM_best_placed_data_center[0]['name']

    def _calculate_extra_DE_needed_when_DM_place_in_current_data_center(self, data_centers, current_data_center, DE_capacity, DM_capacity):
        DE_number_when_DM_place_in = self._calculate_DE_extra_needed(current_data_center, DE_capacity, DM_capacity)
        DE_number_on_others_data_centers = self._calculate_DE_extra_in_others_data_centers(data_centers, current_data_center, DE_capacity)
        return DE_number_when_DM_place_in + DE_number_on_others_data_centers

    def _is_needed_less_extra_DE(self, minimum_extra_DE_amount, total_DE_extra_number):
        return  minimum_extra_DE_amount is None or total_DE_extra_number < minimum_extra_DE_amount[0]

    def _is_needed_the_same_extra_DE(self, minimum_extra_DE_amount, total_DE_extra_number):
        return  total_DE_extra_number == minimum_extra_DE_amount[0]

    def _calculate_DE_extra_in_others_data_centers(self, data_centers, current_data_center, DE_capacity):
        others_data_center = [data_center for data_center in data_centers if data_center != current_data_center]
        DE_extra = 0
        for data_center in others_data_center:
            DE_extra += self._calculate_DE_extra_needed(data_center, DE_capacity)
        return DE_extra

    def _calculate_DE_extra_needed(self, data_center, de_capacity, dm_capacity=0):
        minimun_de_extra_number = math.ceil((data_center['servers'] - dm_capacity) / de_capacity)
        if minimun_de_extra_number < 0:
            return 0
        return minimun_de_extra_number
