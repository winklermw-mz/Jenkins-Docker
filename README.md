# Using Jenkins for CI/CD

## Container

This package provides a Docker file that sets up a container that runs Jenkins LTS and Python 3.12. This contains already contains the necessary tools to execute unit tests, collect code coverage data and, if necessary, instanciate build and run Docker containers to integrate other web services to also perform integration tests.

The configuration of the Jenkins container is located in `jenkins/Dockerfile`. To create the container use the provided script `jenkins/build.sh`. Please note, that `JENKINS_HOME` is mounted as well as the application and the web service to be integrated.

## Configuration

The configuration file stored in `app/Jenkinsfile` can be used to setup a new pipeline job. To do this, click in "new item" on the top left corner, then select "pipeline" and choose type "pipeline script from SCM".

Jenkins will automatically check for changes in the VCS of the main app every 15 minutes. If there are changes, the following steps will be executed:

1. Setup the Python environment for the main app
2. Execute unit tests and collect code coverage data
3. Build and run the container that contains the web service
4. Execute integration test in the main app
5. Perform static code analysis
6. Stop and remove the container that contains the web service
7. Evaluate and store results

The build is considered unstable if at least one unit or integration test fails or if code coverage fall below 80%. The build fails if one of the above steps cannot be executed properly.

## Example

In this example the main app contains a calculator class (`app/src/calculator.py`) that provides some arithmetic functions such as addition or subtraction. This functionality is covered by the unit test in `app/tests/unittest/test_calculator.py`.

Additionally, there is a web service `service/app.py` that also provides a route to calculate the square root of a given non-negative number. This functionality is used in the main app and evaluated in `app/tests/integration/test_webservice.py`.
