"""


"""
import sys


class PlugOut_STDOut(PlugOut):
    """ Output to standard out """
    # What we write to
    f = None

    def __enter__(self):
        """ Open the output or whatever begin/end bit is needed """
        self.f = sys.stdout
        return PlugOut.__enter__(self)

    def __exit__(self, type, value, traceback):
        """ All done """
        self.f.flush()

    def writeRow(self, when, **values):
        """ Append a set of values for all columns """
        self.f.write("FIXME\n\n")
