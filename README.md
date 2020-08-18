Dask Demo for the Evening of Python Coding
==========================================

This repository demonstrates a simple use case of [dask](https://dask.org/) for the [evening of python coding](https://github.com/Jacob-Barhak/EveningOfPythonCoding)


INSTALLATION & DEPENDENCIES:
----------------------------
To install:
1. Copy the files in this repository to a directory of choice
2. Install Anaconda from https://www.anaconda.com/download/
3. install dask and distributed: conda install dask distributed -c conda-forge

Dependant libraries are: dask, distributed

It is recommended you use Anaconda, yet other python environments should work as well
This code was tested on Windows 10 Python 3.7.3  with dask 1.2.2 distributed 1.28.0



USAGE:
------

python DaskDemo.py <ClientName> <Repetitions>
* Arguments are optional, if the user specifies no arguments, the program will run locally


EXAMPLES:
---------

### Basic use:
python DaskDemo.py <Client> <Repetitions>
* If the user specifies no arguments, the program will run locally

### Advanced use:

1. Define a local scheduler:

dask-scheduler --host 127.0.0.1

2. Define workers 

dask-worker 127.0.0.1:8786 --nprocs=4

3. Launch a browser and open the dask status viewer address

http://127.0.0.1:8787/status

4. Launch the program

python DaskDemo.py  127.0.0.1:8786 1000


FILES:
------
* DaskDemo.py : Demo python file
* LICENSE : The license file
* Readme.md : The file that you are reading now




DEVELOPER CONTACT INFO:
-----------------------

Please pass questions to:

Jacob Barhak Ph.D.
jacob.barhak@gmail.com
http://sites.google.com/site/jacobbarhak/


LICENSE
-------
MIT License

Copyright (C) 2020 Jacob Barhak

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
