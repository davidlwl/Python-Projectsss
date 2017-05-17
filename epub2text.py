from epub_conversion.utils import get_files_from_path, convert_epub_to_lines, convert_lines_to_text, open_book

book = open_book("Alan Miller, Satoshi Kanazawa Why Beautiful People Have More Daughters From Dating, Shopping, and Praying to Going to War and Becoming a Billionaire.epub")
if book is not None:
    file = open('book.txt', 'ab')
    for sentence in convert_lines_to_text(str(convert_epub_to_lines(book)),book):
        file.write(sentence.encode("utf-8"))
    print("Wrote \"%s\" to disk" % (book))
    file.close()
else:
    print("Couldn't open \"%s\"." % (book))
