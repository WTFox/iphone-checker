import requests


# TODO Add Click CLI
# TODO Upload to pip
# TODO Add notify options

# Carrier
VALID_CARRIERS = [
    'TMOBILE',
    'ATT',
    'SPRINT',
    'VERIZON'
]

# Where to search
ZIPCODES = [
    '92620',
    '92691',
]

# What are we looking for?
DEVICES = {
    # readable name,  parts.0
    '64GB Space Grey': 'MQAQ2LL/A',
    '256GB Space Grey': 'MQAU2LL/A',
    '64GB Silver': 'MQAR2LL/A',
    '256GB Silver': 'MQAV2LL/A',
}

# Base URL
URL = 'https://www.apple.com/shop/retail/pickup-message'
PICKUP_AVAILABLE = 'available'
CARRIER = 'TMOBILE'


def search_stores_in_zipcode(zipcode, device):
    stores_with_device = []
    response = requests.get(URL, params={
        'pl': True,
        'cppart': CARRIER,
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
    return '{} ({}) has the {} in stock.\nCheck the url here:\n{}\n\nor call them @ {}'.format(
        store.get('storeName'),
        store.get('storeDistanceVoText'),
        device_name,
        store.get('reservationUrl'),
        store.get('phoneNumber')
    )


def main():
    assert CARRIER in VALID_CARRIERS

    total_results = []
    for zipcode in ZIPCODES:
        for name, device in DEVICES.items():
            total_results.extend(search_stores_in_zipcode(zipcode, device))

    if not total_results:
        print("No stores near {} have stock. :(".format(
            ', '.join(ZIPCODES),
        ))
    
    for store in set(total_results):
        print(format_store_display(store))


if __name__ == '__main__':
    main()
