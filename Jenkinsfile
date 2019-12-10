pipeline {
    agent none
    stages {
        stage('Build Image') {
            steps {
                script {
                	app = docker.build("darkklin/python-POM-selenium")
                }
            }
        }
        stage('Push Image') {
            steps {
                script {
			        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
			        	app.push("${BUILD_NUMBER}")
			            app.push("latest")
			        }
                }
            }
        }
    }
}