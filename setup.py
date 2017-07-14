from distutils.core import setup

with open('README.md') as f:
    data = f.read()
try:
    import pypandoc
    description = pypandoc.convert(data, 'rst', format='markdown')
except ImportError:
    print("pypandoc conversion failed, readme will not be rendered on PyPI")
    print("(You can ignore this if you're only doing local development)")
    description = data


setup(
    name='FibDB',
    version='0.1.0',
    packages=['fibdb'],
    license='BSD',
    author='Paul Ivanov',
    author_email='pi@berkeley.edu',
    url='https://github.com/ivanov/fibdb',
    description="Efficienct generation and storage of Fibonacci numbers,"
        "1000x faster than Hadoop",
    long_description=description
)
