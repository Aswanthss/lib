from setuptools import setup
import py2exe

setup(
    console=['main.py'],
    options={
        'py2exe': {
            'packages': ['flask', 'sqlite3'],
            'bundle_files': 1,
            'compressed': True,
            'includes': ['flask', 'sqlite3'],
        }
    },
    zipfile=None,
)




