import sys

import click

from .iphone_checker import check_availability, format_store_display
from .utils import VALID_CARRIERS


@click.command()
@click.option('--carrier', '-c', default='TMOBILE', help='Which carrier do you need?')
@click.option('--zipcode', '-z', help='What zipcode to search in?')
def check_x(carrier, zipcode):
    carrier = carrier.upper()
    assert carrier in VALID_CARRIERS

    if not zipcode:
        click.secho("Please provide a valid zipcode", fg="red")
        sys.exit(1)

    total_results = check_availability(carrier, zipcode)
    if not total_results:
        click.secho("No stores near {} have stock. :(".format(zipcode), fg='yellow')
        sys.exit(0)

    click.secho("The following stores have iPhone X's.", fg="green")
    for store in total_results:
        click.echo(format_store_display(store))

    sys.exit(0)


if __name__ == '__main__':
    check_x()
