import requests


from .utils import PART_NUMBERS, VALID_CARRIERS


# Base URL
URL = 'https://www.apple.com/shop/retail/pickup-message'
PICKUP_AVAILABLE = 'available'


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
    device_name = store.get('partsAvailability', {}).values()[0].get('storePickupProductTitle')
    return '{product}\t{store}\t{url}'.format(
        product=device_name,
        store=store.get('storeName'),
        url=store.get('reservationUrl'),
        phone_number=store.get('phoneNumber')
    )


def check_availability(carrier, zipcode):
    assert carrier in VALID_CARRIERS

    total_results = []
    for device in PART_NUMBERS[carrier].values():
        total_results.extend(search_stores_in_zipcode(carrier, zipcode, device))

    return total_results


if __name__ == '__main__':
    pass
