#!/usr/bin/python

import sys
import os
from commands import *

def run_command(cmd):
        print 'Running: "%s"' % cmd
        text = getstatusoutput(cmd)
        print text

def main():
    # print command line arguments
    run_command('ssh -l fmelsak brmpen-cs12-0.us.oracle.com')
    for arg in sys.argv[1:]:
        print arg

if __name__ == "__main__":
    main()
