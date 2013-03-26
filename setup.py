from setuptools import setup, find_packages

setup(
  name='StatHat',
  version='1.1',
  author='Valentin Bora',
  author_email = 'valentin@gosimplysocial.com',
  description = 'StatHat Python client',
  url = "http://",
  license = "MIT",
  packages = find_packages(exclude=['tests']),
  zip_safe = False,
  include_package_data = True,
  package_data = { 
    '': ['*.png'], 
  },
  entry_points = {
  }
)
