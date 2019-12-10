node {
  try {
    stage('Checkout') {
      checkout scm
    }
    stage('Deploy'){
      sh 'docker build -t python-POM-selenium .'
    }
  }
  catch (err) {
    throw err
  }
}