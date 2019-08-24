from setuptools import setup

# install requirements of the project
with open("requirements.txt") as req:
    install_requires = req.read()

setup(name='zen_quotes',
      version="0.0.1",
      description="Zen of Python Quotes",
      url="",
      author="Yuri Mussi",
      author_email="ymussi@gmail.com",
      license="BSD",
      keywords="Yuri Mussi",
      packages=["quotes"],
      zip_safe=False
      )