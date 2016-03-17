from setuptools import setup, find_packages

setup(name='python-wink',
      version='0.6.4',
      description='Access Wink devices via the Wink API',
      url='http://github.com/bradsk88/python-wink',
      author='Brad Johnson',
      license='MIT',
      install_requires=['requests>=2.0'],
      tests_require=['mock'],
      test_suite='tests',
      packages=find_packages(exclude=['dist', 'test*']),
      zip_safe=True)