# Using Jenkins for CI/CD

## Container

This package provides a Docker file that sets up a container that running Jenkins LTS and Python 3.12. This container already contains the necessary tools to execute unit tests, collect code coverage data and, if necessary, build and run Docker containers to integrate other web services to also perform integration tests.

The configuration of the Jenkins container is located in `jenkins/Dockerfile`. To create the container use the provided script `jenkins/build.sh`. Please note, that `JENKINS_HOME` is mounted as well as the application and the web service to be integrated.

## Configuration

The configuration file stored in `app/Jenkinsfile` can be used to setup a new pipeline job. To do this, click in "new item" on the top left corner, then select "pipeline" and choose type "pipeline script from SCM".

Jenkins will automatically check for changes in the VCS of the main app every 15 minutes. If there are changes, the following steps will be executed:

1. Setup the Python environment for the main app
2. Execute unit tests and collect code coverage data
3. Build and run the container that contains the web service
4. Execute integration test in the main app and collect code coverage data
5. Combine code coverage data from unit and integration tests
6. Stop and remove the container that contains the web service
7. Evaluate and store results

The build is considered unstable one of the following conditions holds:

- at least one unit or integration test fails
- code coverage is below 80%
- there are 10 or more issues found in static code analysis in total or if the total number has increased since the last build

The build fails if one of the above steps cannot be executed properly.

## Example

### Main Pipeline

In this example the main app contains a calculator class (`app/src/calculator.py`) that provides some arithmetic functions such as addition or subtraction. This functionality is covered by the unit test in `app/tests/unittest/test_calculator.py`.

Additionally, there is a web service `service/app.py` (running on `http://localhost:5001`) that also provides a route to calculate the square root of a given non-negative number. This functionality is used in the main app. The integration is evaluated in `app/tests/integration/test_webservice.py`.

### Pipeline for Web Service

There is another pipeline for the web service itself. It is also triggered by VCS changes. The pipeline executes the unit tests in `service/tests/unittest/test_square_root.py`, collects code coverage data and perform static code analysis. If this pipeline has been executed successfully the main pipeline is triggered automatically.
