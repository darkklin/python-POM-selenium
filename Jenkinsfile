pipeline {
    agent none
    stages {
        stage('Build Jar') {
            agent {
                docker {
                    image 'python:3.8.0-slim-buster'
                    args '-v $HOME/Python:/root/Python'
                }
            }
            steps {
                 sh 'sudo python --version'
            }
        }
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