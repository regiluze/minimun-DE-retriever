# -*- coding: utf-8 -*-

from retriever.exceptions import (
    MissingRequiredParameterError,
    InvalidTypeParameterError,
    InvalidParameterError,
)

class Validator(object):

    REQUIRED_INPUT_PARAMETERS = ['DM_capacity', 'DE_capacity', 'data_centers']
    DATA_CENTER_REQUIRED_PARAMETERS = ['name', 'servers']

    def run(self, input_data):
        self._raise_error_if_missing_required_parameters(input_data)
        self._raise_error_if_invalid_parameter_type(input_data)
        self._raise_error_if_invalid_parameter_value(input_data)

    def _raise_error_if_missing_required_parameters(self, input_data):
        for parameter in self.REQUIRED_INPUT_PARAMETERS:
            if input_data.get(parameter, None) is None:
                raise MissingRequiredParameterError(parameter)
        self._check_data_centers_required_parameters(input_data['data_centers'])

    def _check_data_centers_required_parameters(self, data_centers):
        for data_center in data_centers:
            self._check_data_center_required_parameters(data_center)

    def _check_data_center_required_parameters(self, data_center):
        for data_center_parameter in self.DATA_CENTER_REQUIRED_PARAMETERS:
            if data_center.get(data_center_parameter, None) is None:
                raise MissingRequiredParameterError('data_centers {}'.format(data_center_parameter))

    def _raise_error_if_invalid_parameter_value(self, input_data):
        if not input_data['data_centers']:
            raise InvalidParameterError('data_centers')
        if input_data['DE_capacity'] <= 0:
            raise InvalidParameterError('DE_capacity')
        if input_data['DM_capacity'] < 0:
            raise InvalidParameterError('DM_capacity')
        self._check_data_centers_data(input_data['data_centers'])

    def _check_data_centers_data(self, data_centers):
        for data_center in data_centers:
            if not data_center['name']:
                raise InvalidParameterError('data_centers name')
            if data_center['servers'] < 0:
                raise InvalidParameterError('data_centers servers')

    def _raise_error_if_invalid_parameter_type(self, input_data):
        if not self._is_int(input_data['DE_capacity']):
            raise InvalidTypeParameterError('DE_capacity')
        if not self._is_int(input_data['DM_capacity']):
            raise InvalidTypeParameterError('DM_capacity')
        self._check_data_centers_parameters_type(input_data['data_centers'])

    def _check_data_centers_parameters_type(self, data_centers):
        for data_center in data_centers:
            if not self._is_int(data_center['servers']):
                raise InvalidTypeParameterError('data_centers servers')

    def _is_int(self, param):
        try:
           param +=1
           return True
        except:
            return False
