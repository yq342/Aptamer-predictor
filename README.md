# Aptamer-predictor
Installation

The Pse-in-One 2.0 package can be run on Linux (64-bit) and Windows (64-bit) operating system. 
The full package and documents of Pse-in-One 2.0 are available at http://bioinformatics.hitsz.edu.cn/Pse-in-One2.0/download. 
Before using Pse-in-One 2.0, the Python software should be first installed and configured. Python 2.7 64-bit is recommended, 
which can be downloaded from https://www.python.org. 

After Python installed, the Python package Numpy should be downloaded and installed from here: http://www.numpy.org/, 
or use the following command if Internet is accessible:
> pip install numpy

For Windows operating system, the Windows 7 or later versions are supported. The next step is the installation and configuration 
of LIBSVM. Extract the package to a directory. After un-zip the downloaded Pse-in-One 2.0 package, make sure that the “libsvm.dll” 
is available in the directory “…\libsvm\windows”

For Linux operating system, the LIBSVM should be configured firstly. Un-zip the Pse-Analysis package to a folder, for example, 
“~/usr”. Navigate to “~/usr/Pse-in-One 2.0/libsvm” directory, and type the command:
> make

After executing successfully, then navigate to “~/usr/ Pse-in-One 2.0/libsvm/python” directory, and type the command:
> make

If gnuplot has not been installed, use the following command lines to install gnuplot:
> sudo apt-get install gnuplot


For more information, please refer to the manual of Pse-in-One 2.0 in "docs" folder.
