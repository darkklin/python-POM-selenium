FROM python:3.8.0-slim-buster

WORKDIR /usr/share/project

COPY requirements.txt /usr/share/project
RUN pip install --no-cache-dir -r requirements.txt

ADD base            base
ADD pages		        pages
ADD tests		      	tests
ADD utilities       utilities
ADD mypy.ini        mypy.ini
ADD pytest.ini      pytest.ini
ADD testdata.csv    testdata.csv

ENTRYPOINT py.test tests/test_suite_demo.py --browser=$browser




