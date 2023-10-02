import sqlite3
from datetime import datetime as dt

error1 = 'This book already exist'
data = "./data.db"
con = sqlite3.connect(data)
cur = con.cursor() 


class Book:
    def __init__(self, title, path, images_path, audio_path):
        self.title = title
        self.path = path
        self.images_path = images_path
        self.audio_path = audio_path
        self.last_opened = dt.today().date()

    def creer(self):
        verf = False
        books = AllBook()
        for book in books:
            if book[0] == self.title and book[1] == self.path:
                verf = True
                print(error1)
        if not verf:
            cur.execute('''INSERT INTO AllPDF VALUES (?,?,?,?,?);''', (self.title, self.path, self.images_path, self.audio_path, self.last_opened))
            con.commit()


def tri(liste):
    x=len(liste)
    for i in range(x):
        for j in range(i, x):
            if liste[j]<liste[i]:
                temp = liste[i]
                liste[i]=liste[j]
                liste[j]=temp
    return liste


def getTheFilename(data, path):
    fn = data.get(path)
    return fn


def getFileName_2(title):
    r = title[:-4]
    r = r.split(' ')
    n = ''
    for x in range(len(r)):
        if x != 0:
            n = f'{n}_{r[x]}'
        else:
            n = r[0]
    return n


def AllBook():
    cur.execute('''SELECT * FROM AllPDF;''')
    books = cur.fetchall()
    return books


def creerImages(filename, path):
    from random import randint
    import pypdfium2 as pdfium
    import PyPDF2
    from os import chdir, mkdir, remove
    from os.path import join, normpath, expanduser, exists
    pdf = pdfium.PdfDocument(path)
    pages = pdf.get_page()
    out = normpath(expanduser('~/documents'))
    chdir(out)
    if exists(join(out, 'Bibliotheque/{filename}')):
        remove(join(out, 'Bibliotheque/{filename}'))
    else:
        mkdir('Bibliotheque/{filename}')
    out = join(out, 'Bibliotheque/{filename}')
    chdir(out)
    for page in pages:
        pil_image = page.render(
            scale = 1,
            rotation=0,
            crop=(0,0,0,0),
        )
        intr = randint(100, 9999)
        title = f'image_{intr}_{filename[0]}_{i}.png'
        img = pil_image.to_pil()
        img.save(title)
    pat = join(out)
    return pat


def creerAudio(p):
    pass
    """ import PyPDF2, pyttsx3
    p = open(p, 'rb')
    pdfReader = PyPDF2.PdfReader(p)
    # speak = pyttsx3.init()
    for pages in range(len(pdfReader.pages)):
        text = pdfReader.pages[pages].extract_text()
        print(text)
        # speak.say(text)
        # speak.runAndWait()
    # speak.stop()"""


def getThePath(data, filename):
    path = data.get(filename)
    return path


def createDataSet(path):
    import os
    liste = {}
    for root, dirs, files in os.walk(path):
        for el in files:
            if el.endswith('.pdf'):
                liste[el] = os.path.join(root, el)
    return liste


def showAll(d):
    allData = {}
    i = 0
    filenames = showAllFiles(d)
    for fn in filenames:
        p = getThePath(d, fn)
        #p_i = creerImages(fn, p)
        i += 1
        name = getFileName_2(fn)
        b = Book(name, p, '', '')
        b.creer()
        allData[name] = [p, '']
    return allData

def showAllFiles(data):
    files = []
    for a in data.keys():
        files.append(a)
    return files


from os import path

path = path.normpath(path.expanduser("~/desktop"))
# data = createDataSet(path)
creerAudio(path)
# showAll(data)