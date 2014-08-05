import sys
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)


def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False  # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30 + colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)

from xml.dom.minidom import parse
from ebooklib import epub
from pathlib import Path
import shutil

poem_dir = Path('poemsimport/scripts/books/')
EXPORT_DIR = 'poemsimport/scripts/temp_data/'
XML_EXPORT_PATRON = EXPORT_DIR + "poem_%s.xml"


def run():
    # Refres temp directory
    shutil.rmtree("poemsimport/scripts/temp_data")
    Path.mkdir(Path("poemsimport/scripts/temp_data"))

    # Ask for file name to user
    print 'The posible books to import are:'
    for item in list(poem_dir.glob('*.epub')):
        print item.name
    BOOK_NAME = raw_input(
        "Please enter the book name (select from above names...): ")

    try:
        book = epub.read_epub(str(poem_dir) + '/' + BOOK_NAME)

        for index, item in enumerate(book.get_items()):
            if item.get_type() is 9:
                Path(XML_EXPORT_PATRON % index).open('w')\
                    .write(str(item.get_content()).decode('utf-8'))

        printout("SUCCES: Imported ebook ---> %s <--- OK!!!" %
                 BOOK_NAME, GREEN)
    except:
        printout("ERROR: Wrong file name!!!", RED)
