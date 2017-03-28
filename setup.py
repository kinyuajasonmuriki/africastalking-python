from distutils.core import setup
import sys
import os

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='AfricastalkingGateway',
    version='1.7',
    packages=['africastalking'],
    description='An Official Python library for communicating with the AfricasTalking REST API',
    author='Ian Juma',
    install_requires=[
        'requests'
    ],
    author_email='ijuma@africastalking.com',
    url='https://github.com/AfricasTalkingLtd/africastalking-python',
    download_url='https://codeload.github.com/AfricasTalkingLtd/africastalking-python/tar.gz/1.6',
    keywords=['ussd', 'voice', 'sms', 'mpesa', 'payments', 'africastalking'],
    classifiers=[],
)
