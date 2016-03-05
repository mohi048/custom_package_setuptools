import setuptools
setuptools.setup(
name="myproj", # Name of the project
version = "1.0",
packages=setuptools.find_packages()
)

#install dependencies
install_requires = ['configparser','mod_wsgi']

author = "Mohit"
Email = "mohit.048@gmail.com"