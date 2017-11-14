import requests


# Carrier
cppart = 'TMOBILE/US'

# Where to search
zipcodes = ['92620', '92691']

# What are we looking for?
devices = {
    # readable name,  parts.0
    '64GB Space Grey': 'MQAQ2LL/A',
    '256GB Space Grey': 'MQAU2LL/A',
    '64GB Silver': 'MQAR2LL/A',
    '256GB Silver': 'MQAV2LL/A',
}

# No idea what this is...
pl = True

# base url
url = 'https://www.apple.com/shop/retail/pickup-message'


def do_search(zipcode, device):
    response = requests.get(url, params={
        'pl': pl,
        'cppart': cppart,
        'location': zipcode,
        'parts.0': device
    })

    for store in response.json().get('body', {}).get('stores', []):
        if has_iphone(store, device):
            print(format_store_display(store))


def has_iphone(store, device):
    status_dict = store.get('partsAvailability', {}).get(device, {})
    if status_dict.get('pickupDisplay', '') == 'unavailable':
        return False
    else:
        return True


def format_store_display(store):
    return '{}({}) has the iphone in stock. Check the url here\n{}\nor call them @ {}'.format(
        store.get('storeName'),
        store.get('storeDistanceVoText'),
        store.get('reservationUrl'),
        store.get('phoneNumber')
    )


if __name__ == '__main__':
    for zipcode in zipcodes:
        for name, device in devices.items():
            do_search(zipcode, device)
