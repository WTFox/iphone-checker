from distutils.core import setup

setup(
    name='checkx',
    version='0.4',
    packages=['iphone_checker'],
    url='https://github.com/wtfox/iphone-checker',
    license='MIT',
    author='anthonyfox',
    author_email='anthonyfox1988@gmail.com',
    description='',
    py_modules=['iphone_checker'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        checkx=iphone_checker:checkx
    ''',
)
