import json


def test_prediction(client):
    url = '/predict'

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    mock_request_data = {
        'url': ' https://picsum.photos/200/300'
    }

    response = client.post(url, data=json.dumps(mock_request_data), headers=headers)

    json_data = json.loads(response.data)
    first_pred = json_data[0][0]

    assert len(first_pred) == 3

