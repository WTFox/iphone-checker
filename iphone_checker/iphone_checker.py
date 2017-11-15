import requests


from .utils import PART_NUMBERS


URL = 'https://www.apple.com/shop/retail/pickup-message'
PICKUP_AVAILABLE = 'available'


def check_availability(carrier, zipcode):
    carrier = carrier.upper()
    assert carrier in PART_NUMBERS.keys()

    total_results = []
    for device in PART_NUMBERS[carrier].values():
        results = search_stores_in_zipcode(carrier, zipcode, device)
        total_results.extend(results)

    return total_results


def search_stores_in_zipcode(carrier, zipcode, device):
    stores_with_device = []
    response = requests.get(URL, params={
        'pl': True,
        'cppart': carrier,
        'location': zipcode,
        'parts.0': device
    })

    for store in response.json().get('body', {}).get('stores', []):
        if store_has_device(store, device):
            stores_with_device.append(store)

    return stores_with_device


def store_has_device(store, device):
    device_dict = store.get('partsAvailability', {}).get(device, {})
    return device_dict.get('pickupDisplay', '') == PICKUP_AVAILABLE


def format_store_display(store):
    device_name = list(store.get('partsAvailability', {}).values())[0].get('storePickupProductTitle')
    return '{product}\t{store}\t{phone_number}\t{url}'.format(
        product=device_name,
        store=store.get('storeName'),
        url=store.get('reservationUrl'),
        phone_number=store.get('phoneNumber')
    )


if __name__ == '__main__':
    pass
