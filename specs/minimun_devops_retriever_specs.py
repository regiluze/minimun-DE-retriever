# -*- coding: utf-8 -*-

from expects import expect, equal
from retriever.minimun_de_retriever import MinimunDevopsEngineerRetriever

DATA_CENTER_NAME = 'irrelevant-data-center-name'
ANOTHER_DATA_CENTER_NAME = 'another-irrelevant-data-center-name'

with describe('Minimun devops engineer retriever'):
    with before.each:
        self.retriever = MinimunDevopsEngineerRetriever()
    with context('when processing the input data'):
        with context('when there is only one data center'):
            with it('returns the data center name as best place to be devops manager in'):
                data_centers =  [{'name': DATA_CENTER_NAME, "servers": 62 }]

                _, minimun_DE_extra_amount = self.retriever.process(DM_capacity=20, DE_capacity=10, data_centers=data_centers)

                expect(minimun_DE_extra_amount).to(equal(DATA_CENTER_NAME))

            with it('returns 1 as minimum devops extra needed'):
                data_centers = [{'name': DATA_CENTER_NAME, "servers": 30 }]

                minimum_DE_extra_amount, _ = self.retriever.process(DM_capacity=20, DE_capacity=10, data_centers=data_centers)

                expect(minimum_DE_extra_amount).to(equal(1))

            with context('when data center server number of servers doesnt match exactly with DE capacity'):
                with it('returns the minimum up rounded'):
                    data_centers = [{'name': DATA_CENTER_NAME, "servers": 31 }]

                    minimum_DE_extra_amount, _ = self.retriever.process(DM_capacity=20, DE_capacity=10, data_centers=data_centers)

                    expect(minimum_DE_extra_amount).to(equal(2))

            with context('when data center server number of servers is less than DM capacity'):
                with it('returns zero as extra DE needed'):
                    data_centers = [{'name': DATA_CENTER_NAME, "servers": 10 }]

                    minimum_DE_extra_amount, _ = self.retriever.process(DM_capacity=20, DE_capacity=10, data_centers=data_centers)

                    expect(minimum_DE_extra_amount).to(equal(0))

        with context('when there are two data center'):
            with it('returns the minimum extra DE needed'):
                data_centers = [{'name': DATA_CENTER_NAME, 'servers': 62 },
                                {'name': ANOTHER_DATA_CENTER_NAME, 'servers': 20}]

                minimum_DE_extra_amount, _ = self.retriever.process(DM_capacity=20, DE_capacity=8, data_centers=data_centers)

                expect(minimum_DE_extra_amount).to(equal(8))

            with it('returns the best data center name to place the DM in'):
                data_centers = [{'name': DATA_CENTER_NAME, 'servers': 62 },
                                {'name': ANOTHER_DATA_CENTER_NAME, 'servers': 20}]

                _, DM_data_center_name = self.retriever.process(DM_capacity=20, DE_capacity=8, data_centers=data_centers)

                expect(DM_data_center_name).to(equal(ANOTHER_DATA_CENTER_NAME))

        with context('when there is more than one best data center to place DM'):
            with _it('I dont know what to do'):
                data_centers =  [{'name': DATA_CENTER_NAME, "servers": 62 }]

                _, minimun_DE_extra_amount = self.retriever.process(DM_capacity=20, DE_capacity=10, data_centers=data_centers)

                expect(minimun_DE_extra_amount).to(equal(DATA_CENTER_NAME))
