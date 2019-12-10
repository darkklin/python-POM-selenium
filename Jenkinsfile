node {
  try {
    stage('Checkout') {
      checkout scm
    }
    stage('Deploy'){
      app = docker.build("darkklin/python-pom-selenium")
    }
	 stage('Push Image'){
        script {
			    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
			        	app.push("${BUILD_NUMBER}")
			            app.push("latest")
			        }
                }
            
    }
	
  }
  catch (err) {
    throw err
  }
}