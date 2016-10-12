from setuptools import setup
setup(name='cleanslate',
      version='0.2',
      description='Say Goodbye to browser history as you always wanted i.e selectively removing the browsing history',
      url='http://github.com/zuck007/CleanSlate',
      author='Pradeep Khileri',
      author_email='pradeepchoudhary009@gmail.com',
      license='MIT',
      packages=['cleanslate'],
      package_data={'cleanslate': ['*.txt']},
      scripts=['bin/cleanslate'],
      install_requires=[],
      include_package_data=True,
      zip_safe=False)
