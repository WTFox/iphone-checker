
# iPhone X Stock Chcker

This installs a CLI `checkx` that will check nearby apple stores for locations that have the iPhoneX instock.

## Installation

``` bash
$ pip install iphone-checker
```

or Just download or clone this project, `cd` into the dir then run

``` bash 
$ python setup.py install
```

or 

``` bash
$ pip install .
```

## Usage
### Module Usage
```python
In [1]: from iphone_checker import check_availability

In [2]: check_availability('tmobile', '92620')
Out[2]: []  # Too accurate
```

### CLI usage
```
$ checkx -z 92620
No stores near 92620 have stock. :(

$ checkx --help
Usage: checkx [OPTIONS]

Options:
  -c, --carrier TEXT  Which carrier do you need?
  -z, --zipcode TEXT  What zipcode to search in?
  --help              Show this message and exit.
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

MIT: [http://rem.mit-license.org](http://rem.mit-license.org)
