from abc import ABC, abstractmethod
import os
from importlib import import_module
import subprocess


class Report(ABC):

    def __init__(self, file_id):
        """

        :param file_id: id of the file in the database
        """
        self._file_id = None
        self._name = None
        self._cwd = "C:\\git_hub\\reports\\processes"
        self._file_path = None
        self._type = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, val):
        self._file_id = val

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, val):
        self._type = val

    @property
    def file_path(self):
        """

        :return: <string> file path or module name that is needed for handler
        """
        if self.type == "py":
            return "processes.py.{}".format(self.name.replace(".py", ""))
        else:
            return "{cwd}\\{type}\\{filename}".format(cwd=self._cwd, type=self.type, filename=self.name)

    def handle(self, *args):
        """
        call the class method that handles the type of report
        :return:
        """
        print(self.file_path)
        func = getattr(self, '_handle_{}'.format(self.type))
        func(*args)

    def _handle_sql(self, *args, **kwargs):
        """
        reads the sql statement from the file and executes against at database
        :param kwargs: keyword arguments to be passed into the run method
        :param args: list of arguments to be passed into the run method
        :return:
        """
        with open(self.file_path, 'r') as f:
            statement = f.read()
        print(statement)

    def _handle_py(self, *args, **kwargs):
        """
        imports the python module and executes the run method defined in the module
        :param kwargs: keyword arguments to be passed into the run method
        :param args: list of arguments to be passed into the run method
        :return:
        """
        mod = import_module(self.file_path)
        func = getattr(mod, "run")
        func()

    def _handle_sh(self, *args, **kwargs):
        # subprocess.call(['ls', "-l"])
        subprocess.call(['bash', self.file_path], shell=True)

