docker build -t jenkins-python-312 .

docker run -d \
  --name jenkins-python \
  --privileged \
  -u root \
  -p 8080:8080 -p 50000:50000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /Users/markus/storage/jenkins:/var/jenkins_home \
  -v /Users/markus/dev/Jenkins/app:/var/jenkins_workspace_local \
  -v /Users/markus/dev/Jenkins/service:/var/jenkins_service_local \
  -e JAVA_OPTS="-Dhudson.plugins.git.GitSCM.ALLOW_LOCAL_CHECKOUT=true" \
  jenkins-python-312 \
  /bin/bash -c "chmod 666 /var/run/docker.sock && /usr/bin/tini -- /usr/local/bin/jenkins.sh"