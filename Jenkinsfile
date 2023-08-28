pipeline {
  agent any
  stages {
    stage('Checkout') {
            steps {
                // Checkout code from version control
                checkout scm
            }
        }
    stage('Test') {
      steps{
      sh 'docker-compose build'
      sh 'docker-compose up -d'
      sh 'docker cp test.py selenium/standalone-chrome:/app'
      sh 'docker-compose exec selenium/standalone-chrome python test.py'
      }
    }
  }
  post {
        always {
            // Stop and remove all containers
            sh 'docker-compose down'
        }
    }
}
