from ebooklib import epub
from goose import Goose


def run():
    g = Goose()
    article = g.extract(raw_html='/Users/Antonio/Devel/mepoe/mepoe/text.html')
    print article.cleaned_text[:150]
