pipeline {
  agent none
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
      sh 'docker cp . selenium/standalone-chrome:/app'
      sh 'docker-compose exec selenium-tests python your_selenium_script.py'
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
