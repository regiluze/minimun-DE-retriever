# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_cors import CORS

from retriever.validator import Validator
from retriever.minimun_de_retriever import MinimunDevopsEngineerRetriever
from retriever.exceptions import (
        MissingRequiredParameterError,
        InvalidTypeParameterError,
        InvalidParameterError,
        )

BASE_PATH = '/de-minumum-retriever'
app = Flask(__name__)
CORS(app)


@app.route(BASE_PATH, methods=['PUT'])
def minimun_devops_engineer_extra_needed_service():
    input_data = request.get_json()

    try:
        Validator().run(input_data)
        minimum_extra_DE, data_center_name = MinimunDevopsEngineerRetriever().process(input_data['DM_capacity'],
                                                                                      input_data['DE_capacity'],
                                                                                      input_data['data_centers'])
        result = {'DE': minimum_extra_DE, 'DM_data_center': data_center_name}
        return jsonify(result),200, {'content-type':'application/json'}
    except (MissingRequiredParameterError,
            InvalidParameterError,
            InvalidTypeParameterError) as exc:
        error = {'msg': '{}-{}'.format(type(exc),exc)}
        return jsonify(error),400, {'content-type':'application/json'}
    except Exception as exc:
        error = {'msg': '{}-{}'.format(type(exc),exc)}
        return jsonify(error),500, {'content-type':'application/json'}



if __name__ == '__main__':
    app.run()
