from setuptools import setup

setup(name='Python_Utilities',
      version='0.1.7',
      description='A simple test package',
      long_description=open('README.md').read(),
      url='https://github.com/Redstoneur/Python-Utilities',
      author='Alipio SIMOES',
      author_email='alfa.aog36@gmail.com',
      license='Other/Proprietary License',
      packages=['Utilities',
                'Utilities.Calendar',
                'Utilities.FileAndFolder', 'Utilities.FileAndFolder.ReadFile',
                'Utilities.Tools',
                ],
      keywords='test package',
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.10',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Utilities'
      ],
      install_requires=[],
      include_package_data=True
      )
