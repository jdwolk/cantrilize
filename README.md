# Cantrilize

Helps with taking notes for Adrian Cantrill's [AWS Certified Solutions Architect - Associate (SAA-C02 & SAA-C03) course](https://learn.cantrill.io/p/aws-certified-solutions-architect-associate-saa-c02)

## Install

You Should probably install in your global python env rather than a
virtual env so that the symlink in the following step will always work.
(*Or just always remember to switch into the appropriate python env before running?)

```
$ pip install -r requirements.txt
```

```
$ chmod +x ./cantrilize.py
```

```
$ cd <A LOCATION ON YOUR PATH>; ln -s <THIS PROJECT ROOT DIR>/cantrilize.py ./cantrilize
```

## Usage

Meant to be run from inside a directory where you want to make subdirs for each lecture.
For example:

```
~/aws-course
  |_ 01_introduction
    |_ (run from in here to create subdirs for each lecture in section 1)
```

Command:

```
$ cantrilize <CANTRILL COURSE LECTURE URL>
```

, ie:

```
$ cantrilize https://learn.cantrill.io/courses/730712/lectures/25141552
```

This will do 2 things:
1. Create an auto-numbered directory named after the lecture header (eg `09_Network_Starter_Pack___3___Network___Part_2`)
2. Copy the lecture header to your clipboard so you can paste into your notes (eg `10 Network Starter Pack - 3 - Network - Part 2`)
