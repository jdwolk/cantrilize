#!/usr/bin/env python

from argparse import ArgumentParser
import os
import re

from bs4 import BeautifulSoup as BeautifulSoup
import pyperclip
import requests

def parse(page):
    return BeautifulSoup(page.content, 'html.parser')

def underscore(s):
    return re.sub('\s|\-', '_', s)

def zero_pad(num):
    return f'0{num}' if num <= 9 else num

def run(lecture_url: str):
    current_dir = os.getcwd()
    chapter_dirs = [d for d in os.listdir(current_dir) if os.path.isdir(d)]

    last_chapter = None
    try:
        last_chapter = list(reversed(sorted(chapter_dirs)))[0].split("_")[0]
    except IndexError:
        last_chapter = '00'

    last_chapter_num = int(last_chapter)
    this_chapter_num = last_chapter_num + 1
    this_chapter = zero_pad(this_chapter_num)

    page = requests.get(lecture_url)
    contents = parse(page)
    lecture_heading = contents.find(id='lecture_heading').text.strip()

    new_lecture_dir_name = f'{this_chapter}_{underscore(lecture_heading)}'
    print(f'### Creating dir {new_lecture_dir_name}')
    os.mkdir(os.path.join(current_dir, new_lecture_dir_name))

    notes_heading = f'{this_chapter} {lecture_heading}'
    pyperclip.copy(notes_heading)
    print(f'### Copied chapter header to clipboard:')
    print(notes_heading)


description = ("Helps with notetaking for Adrian Cantrill's AWS courses. " +
              "Creates a numbered dir in the current dir for the given chapter " +
              "(ie '10_Network_Starter_Pack___3___Network___Part_2') and " +
              "copies the chapter header to the clipboard so you can paste into your notes " +
              "(ie '10 Network Starter Pack - 3 - Network - Part 2')")

parser = ArgumentParser(description=description)
parser.add_argument('lecture_url', type=str, nargs=1, help='The URL to the current lecture')
args = parser.parse_args()

run(args.lecture_url[0])
