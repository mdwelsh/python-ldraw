import tempfile
import os

from ldraw.config import write_config
from ldraw.download import download_main
from ldraw.tools import image_size, vector_position
from ldraw.tools.ldr2inv import ldr2inv
from ldraw.tools.ldr2png import ldr2png
from ldraw.tools.ldr2pov import ldr2pov
from ldraw.tools.ldr2svg import ldr2svg

INPUT_PATH = 'tests/test_data/car.ldr'

download_main('tmp')
write_config({'parts.lst': os.path.join('tmp', 'ldraw', 'parts.lst')})


def tool_test(func, suffix):
    fd, file = tempfile.mkstemp(suffix=suffix)
    func(file)
    content = open(file, 'r').read()
    # uncomment to save content to expected
    # open('tests/test_data/car' + suffix, 'w').write(content)

    expected = open('tests/test_data/car' + suffix).read()
    assert expected == content


def test_ldr2inv():
    tool_test(lambda f: ldr2inv(INPUT_PATH, f), '.inv')


def test_ldr2png():
    tool_test(lambda f: ldr2png(INPUT_PATH, f, vector_position('0,0,0'), vector_position('100,100,100'), 50,
                                image_size('800x800'), '#FF0000', '#123456'), '.png')


def test_ldr2pov():
    tool_test(lambda f: ldr2pov(INPUT_PATH, f,
                                vector_position('100,100,100'),
                                vector_position('0,0,0'),
                                '#123456'), '.pov')


def test_ldr2svg():
    tool_test(lambda f: ldr2svg(INPUT_PATH, f,
                                image_size('800x800'),
                                vector_position('100,100,100'),
                                vector_position('0,0,0'),
                                '#123456', False), '.svg')


def test_ldr2svg_qt():
    tool_test(lambda f: ldr2svg(INPUT_PATH, f,
                                image_size('800x800'),
                                vector_position('100,100,100'),
                                vector_position('0,0,0'),
                                '#123456', True), '.qt.svg')
