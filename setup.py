from setuptools import setup

setup(name='funchain',
      version='0.0.1-alpha.1',
      description='Functional processing for Python without the hassle of variable handling.',
      classifiers=[
            'Development Status :: 1 - Planning',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.8',
            'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      url='http://github.com/eugenma/funchain',
      author='Eugen Massini',
      author_email='eugen@massini.de',
      license='MIT',
      tests_require=['pytest', ],
      packages=['funchain'],
      zip_safe=False)
