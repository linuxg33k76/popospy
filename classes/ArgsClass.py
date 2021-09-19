#!/usr/bin/env python3



import argparse


class CLIParser(argparse.ArgumentParser):

    '''
    --------------------------------------------------------------------------------
    Description:  Collect cli arguments and present help commands - an extension
    of argparse.ArgumentParser() class.
    Parameter(s):  None
    Return: None.
    --------------------------------------------------------------------------------
    '''

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-s', '--skip', type=str, help='Skip specific task:  3rdParty, update, InstallPkg', default='')
        self.parser.add_argument('-e', '--exclude', type=str, help='Exclude Specified Packages from package file', default='', nargs="+")
        self.parser.add_argument('-f', '--file', type=str, help='Specify Package File (*.json)', default='')
        self.parser.add_argument('-v', '--verbose', help='Display log file output', action='store_true')
        self.parser.add_argument('--test', help='Turn on test output', action='store_true')
        self.parser.add_argument('-l', '--list', type=str, help='Display systems: dev, production, all', default='')
        self.args = self.parser.parse_args()
        self.task = self.args.task

    def get_args(self):

        '''
        --------------------------------------------------------------------------------
        Description:  Return cli arguments.
        Parameter(s):  self : instance of CLIParser() class
        Return: self.args : object
        --------------------------------------------------------------------------------
        '''

        return self.args
