from setuptools import setup

README = open('README.md').read()

setup(
        name='lektor-gist',
        author='Anthony Plunkett',
        author_email='anthony@thefort.org',
        url='https://github.com/doobeh/lektor-gist',
        version='0.1.0',
        license='BSD',
        description='Embed Gist snippets in your articles',
        long_description=README,
        py_modules=['lektor-gist'],
        entry_points={
            'lektor.plugins': [
                'gist=lektor_gist:GistPlugin',
            ]
        },
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ], requires=['lektor']
)