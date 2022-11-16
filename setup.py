from setuptools import setup

setup(name='yugioh',
      version='1.0.0',
      description='Very Thin Yu-Gi-Oh API Wrapper',
      long_description=open('README.rst').read(),
      url='https://github.com/EllieJaybee/yugioh',
      author='elliejaybee',
      author_email='ellie@femboy.my',
      install_requires=['requests'],
      packages=['yugioh'],
      keywords='Yu-Gi-Oh API')
