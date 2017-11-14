
# iPhone X Stock Chcker

This installs a CLI `checkx` that will check nearby apple stores for locations that have the iPhoneX instock.

## Installation

Just download or clone this project, `cd` into the dir then run

``` bash 

    python setup.py install
```

or 

``` bash

    pip install .
```

## Usage
Note: When running it the first time it will ask you to enter login credentials.
``` bash
$ checkx --help
Usage: checkx [OPTIONS]

Options:
  -c, --carrier TEXT  Which carrier do you need?
  -z, --zipcode TEXT  What zipcode to search in?
  --help              Show this message and exit.
```

## TODO
- [] Upload to pip
- [] Add notify options

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

Nothing to see here yet folks

## License

MIT: [http://rem.mit-license.org](http://rem.mit-license.org)
