# Homework 7 (uses v2/api/<endpoint>)
## Running the server
To run the server, follow the instructions in the readme page.

## API description
This service lets us simply retrieve a list of tours, and a tour itself.
The endpoints for this service are:
<ul>
	<li><a  href="http://127.0.0.1:8000/v2/api/tours/">v2/api/tours</a></li>
    <li><a  href="http://127.0.0.1:8000/v2/api/tours/8">v2/api/tours/id</a></li>
</ul>

### /tours
This endpoints uses weak ETags, meaning that it only considers modification to names or the ID's of the tours, but doesn't
consider modifications to the location of the tour.

The available operations are:
<b>GET</b>
<i>request</i>

> GET /tours
> If-None-Match: ...

<i>response if ETag matches</i>

> 304 not modified
> ETag: ...

<i>response if ETag doesn't match</i>

> 200 ok
> ETag: ...

<b>POST</b>
<i>request</i>

> POST /tours
> name: ...
> location: ...

<i>response</i>

> 201 Created
> resource
> ETag: ...


### /tours/id
This endpoint uses strong ETags, meaning that it takes into consideration the whole resource. If anything about the resource changes, than the ETag will also change with it.

The available operations are:
<b>GET</b>
<i>request</i>

> GET /tours/id
> If-None-Match: ...

<i>response if ETag matches</i>

> 304 not modified
> ETag: ...

<i>response if ETag doesn't match</i>

> 200 ok
> resource
> ETag: ...

