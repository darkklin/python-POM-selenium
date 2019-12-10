pipeline {
    agent none
    stages {
        stage('Build Image') {
            steps {
                script {
                	sh 'docker build -t darkklin/python-pom-selenium .'
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