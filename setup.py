from distutils.core import setup
from setuptools import find_packages

setup(
    name='django_admin_terminal',
    description='bash console in the browser for django admins',
    keywords='django, bash, terminal, console, server',
    packages=find_packages(),
    include_package_data=True,
    version="0.5.1",
    author="Assem Chelli",
    author_email="assem.ch@gmail.com",
    url='http://github.com/assem-ch/django-admin-terminal',
    classifiers=[
                    'Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: GNU General Public License (GPL)',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Internet :: WWW/HTTP',
                 'Topic :: Software Development :: Libraries :: Application Frameworks',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 ],
    license="BSD License",
    platforms=["all"],
    zip_safe=False
)
