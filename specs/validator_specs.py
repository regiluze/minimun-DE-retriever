# -*- coding: utf-8 -*-

from expects import *


with describe('Rest API input data validator spec'):
    with before.each:
        self.validator = Validator()

    with context('checking required parameters'):
        with context('when DM_capacity is missing'):
            with it('raises a MissingRequiredParameterError'):
                input_data = {'DE_capacity': 4, 'data_centers': [{'name': 'a_name', 'servers': 20}]}

                def _missing_DM_capacity():
                    self.validator.run(input_data)

                expect(_missing_DM_capacity).to(raise_error(MissingRequiredParameterError, 'DM_capacity'))

        with context('when DE_capacity is missing'):
            with it('raises a MissingRequiredParameterError'):
                input_data = {'DM_capacity': 4, 'data_centers': [{'name': 'a_name', 'servers': 20}]}
                validator = Validator()

                def _missing_DE_capacity():
                    self.validator.run(input_data)

                expect(_missing_DE_capacity).to(raise_error(MissingRequiredParameterError, 'DE_capacity'))

        with context('when data_centers is missing'):
            with it('raises a MissingRequiredParameterError'):
                input_data = {'DM_capacity': 4, 'DE_capacity': 4}
                validator = Validator()

                def _missing_data_centers():
                    self.validator.run(input_data)

                expect(_missing_data_centers).to(raise_error(MissingRequiredParameterError, 'data_centers'))

        with context('when data_center parameter is missing'):
            with context('when name parameter is missing'):
                with it('raises a MissingRequiredParameterError'):
                    input_data = {'DM_capacity': 4, 'DE_capacity': 4, 'data_centers': [{'servers': 20}]}
                    validator = Validator()

                    def _missing_data_center_name():
                        self.validator.run(input_data)

                    expect(_missing_data_center_name).to(raise_error(MissingRequiredParameterError, 'data_centers name'))

            with context('when servers parameter is missing'):
                with it('raises a MissingRequiredParameterError'):
                    input_data = {'DM_capacity': 4, 'DE_capacity': 4, 'data_centers': [{'name': 'a_name'}]}
                    validator = Validator()

                    def _missing_data_center_name():
                        self.validator.run(input_data)

                    expect(_missing_data_center_name).to(raise_error(MissingRequiredParameterError, 'data_centers servers'))

    with context('checking invalid values'):
        with context('when data_centers is an empty list'):
            with it('raises a InvalidParameterError'):
                input_data = {'DE_capacity': 4, 'DM_capacity': 4, 'data_centers': []}

                def _invalid_data_centers_value():
                    self.validator.run(input_data)

                expect(_invalid_data_centers_value).to(raise_error(InvalidParameterError, 'data_centers'))

        with context('when DE_capacity is zero'):
            with it('raises a InvalidParameterError'):
                input_data = {'DE_capacity': 0, 'DM_capacity': 4, 'data_centers': [{'name': 'a_name', 'servers': 20}]}

                def _DE_capacity_value_is_zero():
                    self.validator.run(input_data)

                expect(_DE_capacity_value_is_zero).to(raise_error(InvalidParameterError, 'DE_capacity'))

        with context('when DE_capacity a negative number'):
            with it('raises a InvalidParameterError'):
                input_data = {'DE_capacity': -1, 'DM_capacity': 4, 'data_centers': [{'name': 'a_name', 'servers': 20}]}

                def _DE_capacity_value_is_negative():
                    self.validator.run(input_data)

                expect(_DE_capacity_value_is_negative).to(raise_error(InvalidParameterError, 'DE_capacity'))

        with context('when DM_capacity a negative number'):
            with it('raises a InvalidParameterError'):
                input_data = {'DE_capacity': 1, 'DM_capacity': -4, 'data_centers': [{'name': 'a_name', 'servers': 20}]}

                def _DM_capacity_value_is_negative():
                    self.validator.run(input_data)

                expect(_DM_capacity_value_is_negative).to(raise_error(InvalidParameterError, 'DM_capacity'))

        with context('when data centers parameters are invalid'):
            with context('when name is empty string'):
                with it('raises a InvalidParameterError'):
                    input_data = {'DE_capacity': 1, 'DM_capacity': 4, 'data_centers': [{'name': '', 'servers': 20}]}

                    def _data_center_name_is_empty_string():
                        self.validator.run(input_data)

                    expect(_data_center_name_is_empty_string).to(raise_error(InvalidParameterError, 'data_centers name'))

            with context('when servers is negative'):
                with it('raises a InvalidParameterError'):
                    input_data = {'DE_capacity': 1, 'DM_capacity': 4, 'data_centers': [{'name': 'a_name', 'servers': -20}]}

                    def _data_center_servers_is_negative():
                        self.validator.run(input_data)

                    expect(_data_center_servers_is_negative).to(raise_error(InvalidParameterError, 'data_centers servers'))

    with context('checking invalid input types'):
        with context('when DE_capacity is not an Integer'):
            with it('raises a InvalidTypeParameterError'):
                input_data = {'DE_capacity': '4', 'DM_capacity': 4, 'data_centers': [{'name': 'a_name', 'servers': 20}]}

                def _invalid_DE_capacity_type():
                    self.validator.run(input_data)

                expect(_invalid_DE_capacity_type).to(raise_error(InvalidTypeParameterError, 'DE_capacity'))

        with context('when DM_capacity is not an Integer'):
            with it('raises a InvalidTypeParameterError'):
                input_data = {'DE_capacity': 4, 'DM_capacity': '4', 'data_centers': [{'name': 'a_name', 'servers': 20}]}

                def _invalid_DM_capacity_type():
                    self.validator.run(input_data)

                expect(_invalid_DM_capacity_type).to(raise_error(InvalidTypeParameterError, 'DM_capacity'))

        with context('when data center servers is not an Integer'):
            with it('raises a InvalidTypeParameterError'):
                input_data = {'DE_capacity': 4, 'DM_capacity': 4, 'data_centers': [{'name': 'a_name', 'servers': '20'}]}

                def _invalid_data_centers_servers_type():
                    self.validator.run(input_data)

                expect(_invalid_data_centers_servers_type).to(raise_error(InvalidTypeParameterError, 'data_centers servers'))
