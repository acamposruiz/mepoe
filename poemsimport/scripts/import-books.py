# -*- coding:utf-8 -*-
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
from poems.models import Poem
from django.contrib.auth.models import User

poem_dir = Path('poemsimport/scripts/books/')
EXPORT_DIR = 'poemsimport/scripts/temp_data/'
XML_EXPORT_PATRON = EXPORT_DIR + "poem_%s.xml"


def epub2files():
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


def files2database():
    print 'Exported files:'
    for item in list(Path(EXPORT_DIR).glob('*.xml')):
        body = ''
        try:
            dom = parse(EXPORT_DIR + item.name)
            for h in dom.getElementsByTagName('h3'):
                try:
                    title = h.firstChild.data
                except Exception, e:
                    title = None
            for v in dom.getElementsByTagName('p'):
                try:
                    if len(v.firstChild.data) > 2:
                        body += v.firstChild.data + '/'
                    else:
                        body += '*'
                except Exception, e:
                    body += '*'
            if len(body) > 2:
                import random
                user = User.objects.order_by('?')[0]
                # Add avatar to user
                image_type = random.choice((
                    'abstract', 'animals', 'business', 'cats', 'city', 'food',
                    'nightlife', 'fashion', 'people', 'nature', 'sports',
                    'technics', 'transport'))
                image_url = 'http://lorempixel.com/900/480/abstract/'
                import requests
                import tempfile
                from django.core import files

                # Steam the image from the url
                request = requests.get(image_url, stream=True)

                # Create a temporary file
                lf = tempfile.NamedTemporaryFile(
                    suffix='.jpg',
                    prefix=title)

                # import ipdb
                # ipdb.set_trace()

                # Read the streamed image in sections
                for block in request.iter_content(1024 * 8):

                    # If no more file then stop
                    if not block:
                        break

                    # Write image block to temporary file
                    lf.write(block)

                poem = Poem(
                    user=user, title=title, author='Pablo Neruda',
                    book='Veinte Poemas de Amor y Una Cancion Desesperada',
                    body=body, image=files.File(lf))
                poem.save()
        except Exception, e:
            pass
        else:
            pass
        finally:
            pass


def run():
    epub2files()
    files2database()
