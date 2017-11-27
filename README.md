# its-ok-to-thank

## About

Software for sending automated heartfelt emails to people I am thankful for.

This project is part of my master's thesis [its-ok](https://vimeo.com/216762164) at the [Interactive Telecommunications Program](https://tisch.nyu.edu/itp), [New York University](https://www.nyu.edu/). You can watch the video for a live demo of this software.

## Technology

This software was programmed on Python 2.7 and its dependencies are the Selenium Python module and Chromedriver, which can be installed through homebrew on a mac.

It runs and has been tested on Mac OS X.

## Install dependencies

* Install [Homebrew](https://brew.sh/)

* Install Chromedriver with Homebrew

```bash
brew install chromedriver
```

* Install virtualenv

```bash
pip install virtualenv
```

## Customization

Modify the file example-mails.json

## Executing

* cd to the folder

* Instantiate a virtual environment

```bash
virtualenv env
```
* Activate the instance of the virtual environment

```bash
source env/bin/activate
```

* Install selenium on the virtual environment

```bash
pip install selenium
```

* To run the code

```python
python thank.py
```

* to deactivate the virtual environment and finish
```bash
deactivate
```

## Documentation

![demo](https://github.com/montoyamoraga/its-ok-to-thank/raw/master/documentation/its_ok_to_thank_loop.gif "its-ok-to-thank")

## Thanks

* [Allison Parrish](https://www.decontextualize.com/) for her [Reading and writing electronic text](http://rwet.decontextualize.com/) class
* [Homebrew](https://brew.sh/) for making installation a breeze
* [Sam Lavigne](http://lav.io/) for his [Detourning the web](https://github.com/antiboredom/detourning-the-web) class
