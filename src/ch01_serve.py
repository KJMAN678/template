inference_request = {
    "inputs": [
        {
          "name": "fixed acidity",
          "shape": [14],
          "datatype": "FP32",
          "data": [0. 0. 1. 0. 0. 0. 1. 1. 0. 1. 1. 0. 0. 0.],
        }
    ]
}

endpoint = "http://127.0.0.1:5000/v2/models/wine-classifier/infer"
response = requests.post(endpoint, json=inference_request)

response.json()