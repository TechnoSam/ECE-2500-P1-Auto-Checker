# ECE-2500-P1-Auto-Checker
Automatic Checking script for ECE 2500 (Fall 2017) Project 1

**Tested with Python 2.7.13**

This script will automatically run myAssembler for Project 1 and compare the output to what is expected and report differences.

You can import this as a submodule if you want to take advantage of the default paths, but you can also clone it anywhere and give it the path to your executable or script.

    usage: check.py [-h] (-p | -c) [--path PATH] [-t TESTS] [-o] [-v]

    ECE 2500 Project 1 Auto Checker

    optional arguments:
      -h, --help            show this help message and exit
      -p, --python          Specify that myAssembler is written in python
      -c, --cpp             Specify that myAssembler is written in C++
      --path PATH           Specify the path to the myAssembler script or
                            executable (default "../myAssembler.py" or
                            "../myAssembler")
      -t TESTS, --tests TESTS
                            Specify which tests should be run e.g. "1, 2, 3"
                            (default all)
      -o, --save-output     Save the output with a timestamp (default
                            "last_test.log")
      -v, --verbose         Enable verbose output

Examples:

Run tests 1, 2, and 3 for a python script located at ../myAssembler.py with verbose output, saving to logs/last_test.log.

    python check.py -p --path "../myAssembler.py" -t "1, 2, 3" -v

Run tests 1, 2, and 3, for a C++ executable located at ..\P1\Build\myAssembler.exe with verbose output, saving to logs/last_test.log.

    python check.py -c --path "..\P1\Build\myAssembler.exe" -t "1, 2, 3" -v

Run tests 1, 3, and 5 for a python script located at ../myAssembler.py with verbose output, saving to logs/last_test.log.

    python check.py -p --path "../myAssembler.py" -t "1, 3, 5" -v

Run all tests for a python script located at ../myAssembler.py saving the output to logs/test_{timestamp}.log

    python check.py -p --path "../myAssembler.py" -t -o

If you want to add support for another language or add more tests, contact me and I can give you commit access.

*Note: Windows is weird. The default exe path will probably not work, so just specify it manually if it doesn't. You may need to use a "\" instead of "/" like normal OSes*
