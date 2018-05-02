from setuptools import setup

setup(name='keyholder',
      version='0.2.6',
      description='Wrapper for multiple key-value stores',
      url='https://github.com/s0urc3c0d3/keyholder',
      author='Grzegorz Dwornicki',
      author_email='gd1100@gmail.com',
      license='MIT',
      packages=['keyholder'],
      install_requires=['kazoo','python-etcd','python-interface'],
      zip_safe=False)
