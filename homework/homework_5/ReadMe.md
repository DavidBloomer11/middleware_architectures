# How to run the server

First activate the virtual environment by doing the following commands:


> cd env/scripts

> activate


After, cd back to main directory. To run the server do the following command:

> cd tour_service

> python manage.py runserver


Now the server should be running on <a  href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>.


# Requests

The following base endpoints are defined:
<ul>
	<li><a  href="http://127.0.0.1:8000/api/customers">api/customers</a>
	<li><a  href="http://127.0.0.1:8000/api/tours">api/tours</a>
	<li><a  href="http://127.0.0.1:8000/api/locations">api/locations</a>
    <li><a  href="http://127.0.0.1:8000/api/countries">api/countries</a>
    <li><a  href="http://127.0.0.1:8000/api/customers-on-tours">api/customers-on-tours</a>
</ul>
