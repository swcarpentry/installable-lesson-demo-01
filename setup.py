import os
import glob
from distutils.core import setup

setup(
    name = 'something',
    version = '0.0.1',
    description = 'Exploring ways of managing lessons as Python packages.',
    author = 'Greg Wilson',
    author_email = 'gvwilson@software-carpentry.org',
    license = 'CC-BY/MIT',
    packages=['code'],
    data_files=[('data', glob.glob('data/*.*')),
                (os.curdir, glob.glob('*.html'))],
    scripts=['scripts/lesson']
)
