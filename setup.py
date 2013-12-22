import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'pyramid_beaker',
    'js.bootstrap',
    'js.jquery',
    'pyramid_twitterauth',
    'pyramid_celery',
    'pyramid_fanstatic',
]

setup(name='second_project',
      version='0.0',
      description='second_project',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='second_project',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = second_project:main
      [console_scripts]
      initialize_second_project_db = second_project.scripts.initializedb:main
      """,
      )
