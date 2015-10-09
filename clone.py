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
    umask 022
    run_command('export PATH=/ws/on12-tools/onbld/bin/:/ws/onnv-tools/teamware/bin:/opt/onbld/bin/`uname -p`:/usr/bin:/usr/sbin')
    for arg in sys.argv[1:]:
        print arg

if __name__ == "__main__":
    main()
