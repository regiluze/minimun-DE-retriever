# -*- coding: utf-8 -*-

from expects import *
from retriever.minimun_de_retriever import MinimunDevopsEngineerRetriever

DATA_CENTER_NAME = 'irrelevant-data-center-name'

with describe('Minimun devops engineer retriever'):
    with before.each:
        self.retriever = MinimunDevopsEngineerRetriever()
    with context('when processing the input data'):
        with context('when there is only one data center'):
            with it('returns the data center name as best place to be devops manager in'):
                input_data = {'DM_capacity': 20, 'DE_capacity': 10,
                              'data_centers': [{'name': DATA_CENTER_NAME, "servers": 62 }]}

                result = self.retriever.process(input_data)

                expect(result['DM_data_center']).to(equal(DATA_CENTER_NAME))

            with it('returns 1 as minimun devops extra needed'):
                input_data = {'DM_capacity': 20, 'DE_capacity': 10,
                              'data_centers': [{'name': DATA_CENTER_NAME, "servers": 30 }]}

                result = self.retriever.process(input_data)

                expect(result['DE']).to(equal(1))

            with context('when data center server number of servers doesnt match exactly with DE capacity'):
                with it('returns the minimun up rounded'):
                    input_data = {'DM_capacity': 20, 'DE_capacity': 10,
                                  'data_centers': [{'name': DATA_CENTER_NAME, "servers": 31 }]}

                    result = self.retriever.process(input_data)

                    expect(result['DE']).to(equal(2))

            with context('when data center server number of servers is less than DM capacity'):
                with it('returns zero as extra DE needed'):
                    input_data = {'DM_capacity': 20, 'DE_capacity': 10,
                                  'data_centers': [{'name': DATA_CENTER_NAME, "servers": 10 }]}

                    result = self.retriever.process(input_data)

                    expect(result['DE']).to(equal(0))
