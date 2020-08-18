##############################################################################
# This repository demonstrates a simple use case of dask for the 
# evening of python coding
##############################################################################
# Copyright (C) 2020 Jacob Barhak
#
# Permission is hereby granted, free of charge, to any person obtaining a 
# copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the 
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.
##############################################################################


import dask
import subprocess
import dask.distributed
import os
import random
import sys


if __name__ == '__main__':
    # Create a temporary directory doe files to be stored id does not exist
    TempDir = 'DaskDemoTemp'
    try:
        os.mkdir(TempDir)
        print ('Temporary dir created')
    except:
        print ('Temporary dir already exists')

    # Handle command line arguments or use defaults if not defined
    ClientName = 'None'
    Repetitions = 200
    if len(sys.argv)>1:
        ClientName = sys.argv[1]
    if len(sys.argv)>2:
        Repetitions = int(sys.argv[2])
    
    # Initialize dask client if defined
    if ClientName == 'None':
        DaskClient = None
    else:
        # commenting the next line, makes things work
        DaskClient = dask.distributed.Client(ClientName)

    # define the worked directory as the current directory
    WorkingDir = os.getcwd()
    
    @dask.delayed
    def MapElement(RunNumber):
        "Compute Element"
        os.chdir(WorkingDir)
        # Define file names and files
        FileNameOut = TempDir + os.sep + 'Out%i.txt'%RunNumber
        FileNameErr = TempDir + os.sep + 'Err%i.txt'%RunNumber
        FileNameBatch = TempDir + os.sep + 'Batch%i.bat'%RunNumber
        FileOut = open (FileNameOut,'wb')
        FileErr = open (FileNameErr,'wb')    
        FileBatch = open (FileNameBatch,'w')  
        # Create a script with that will echo random numbers up to 10000
        Random = random.random()
        Script = ''
        for Entry in range(int(10000*Random)):
            Script = Script + 'echo ' + str(Entry) +' \n'  
        FileBatch.write(Script)
        FileBatch.close()
        # Execute the script in a process
        subprocess.call(args = FileNameBatch, stdout = FileOut, stderr = FileErr, shell=True)       
        FileOut.close()  
        FileErr.close()
        # The function returns the output file names
        return FileNameOut
    
    @dask.delayed
    def DelayedReduce(Array):
        "Reduce the array"
        # This function collects the names in the array and output them in a summary file
        OutputFilesStr = ''
        for Entry in Array:
            print (Entry)
            OutputFilesStr = OutputFilesStr + str(Entry) + ' , '
        SummaryFileName = TempDir+os.sep+'Summary.txt'
        FileOut = open (SummaryFileName,'w')
        FileOut.write(OutputFilesStr)
        FileOut.close()
        return (SummaryFileName)
    
    print ('Defined Functions')
    ComputeArray = [ MapElement(Entry) for Entry in range(Repetitions)]
    print ('Created Compute Array')
    Out = DelayedReduce(ComputeArray) 
    print ('Defined Reduce Array')
    SummaryFileName = Out.compute()
    print ('Finished Computation and stored list of files in:')
    print (SummaryFileName)
    # Close the client
    if DaskClient != None:
        DaskClient.close()