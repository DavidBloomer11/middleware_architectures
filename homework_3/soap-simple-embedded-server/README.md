# SOAP Embedded Server

This simple projects runs a Tomcat Web server and deploys a minimal SOAP Web service.
This project follows the CODE-FIRST approach.

## How to run?

* `mvn clean install cargo:run`
* the server will run at port `9090`
* the Web Service configuration is in: `WebContent/WEB-INF/sun-jaxws.xml`

## Test after running

* Summary page [http://localhost:9090/testWebService](http://localhost:9090/testWebService)
* WSDL at [http://localhost:9090/testWebService?wsdl](http://localhost:9090/testWebService?wsdl)

## Tips

* The Web Service connfiguration is available at https://bitbucket.org/m1ci/soap-simple-embedded-server/src/master/WebContent/WEB-INF/sun-jaxws.xml
  * `services.TestService` - here `services` is the package, while `TestService` is the class name that implements the Web Service