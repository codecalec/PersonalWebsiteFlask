# PersonalWebsiteFlask
Personal website created using Flask

It is available at [here](http://www.alexveltman.com)

This repo is archived and outdated since I've ported my site to Python using Flask which can be found [here](https://github.com/codecalec/PersonalWebsiteFlask/)

## About

This is the source code for my personal website. It was written in Python using Flask. The website can be found [here](www.alexveltman.com).

I used the following projects to help get me start:

- [Skeleton](https://github.com/dhg/Skeleton) for a clean interface without messing around too much with CSS
- [python-markdown](https://python-markdown.github.io/) was used to render markdown for resume and blog page

## Installation
The easiest method is to ensure you have [Pipenv](https://pipenv.readthedocs.io/en/latest/) installed.

1. Run `pipenv install` to setup environment in root of project
2. You then need to set the applicaiton for flask to run by using `export FLASKAPP=personalsite.py`
3. Call `flask run` to launch a local server on port 5000
