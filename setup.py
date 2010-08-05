import os, extend_messages
from setuptools import setup, find_packages

if extend_messages.VERSION[-1] == 'final':
    CLASSIFIERS = ['Development Status :: 5 - Stable']
elif 'beta' in extend_messages.VERSION[-1]:
    CLASSIFIERS = ['Development Status :: 4 - Beta']
else:
    CLASSIFIERS = ['Development Status :: 3 - Alpha']

CLASSIFIERS += [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

setup(
    author = extend_messages.__maintainer__,
    author_email = extend_messages.__email__,
    name = 'django-extend-messages',
    version = extend_messages.__version__,
    description = 'Extend version of django.contrib.messages',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url = 'http://github.com/Anber/django-extend-messages/tree/master',
    license = 'BSD License',
    platforms=['OS Independent'],
    classifiers = CLASSIFIERS,
    requires=[
        'django (>1.2.0)',
    ],
    packages=find_packages(),
    zip_safe=False
)