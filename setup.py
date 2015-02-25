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
    data_files=[('lessons/something/data', glob.glob('data/*.*')),
                ('lessons/something/code', glob.glob('code/*.*')),
                ('lessons/something',      glob.glob('*.html')),
                ('lessons/something/css',  glob.glob('css/*.*'))],
    scripts=['scripts/lesson']
)
