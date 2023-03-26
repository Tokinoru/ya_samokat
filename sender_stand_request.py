import configuration
import requests
import data


def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)


response = create_new_order(data.order_body)
print(response.status_code)
print(response.json())


def get_order(track_id: int):
    request_params = {"t": track_id}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK,
                        params=request_params,
                        headers=data.headers)


response = get_order(867704)
print(response.status_code)
print(response.json())

assert response.status_code == 200
