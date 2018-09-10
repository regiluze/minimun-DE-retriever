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

app = Flask(__name__)
CORS(app)


@app.route("/kk", methods=['PUT'])
def minimun_devops_engineer_extra_needed_service():
    input_data = request.get_json()

    try:
        Validator().run(input_data)
        result = MinimunDevopsEngineerRetriever().process(input_data['DM_capacity'],
                                                          input_data['DE_capacity'],
                                                          input_data['data_centers'])

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
