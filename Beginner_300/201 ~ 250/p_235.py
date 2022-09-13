from distutils.util import convert_path


def convert_int(string):
    return int(string.replace(',',''))
convert_int("1,234,567")