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
      sh 'docker network create ml_network'
      
      sh 'docker run -d -p 5000:5000 --name backend --network ml_network  kavipriyanjeevanandam/ml-flask:0.1'
      sh 'docker run -p 80:80 --name frontend --network ml_network kavipriyanjeevanandam/ml-angular:0.1' 
      sh 'docker run -d --name seleniumenv --network ml_network selenium/standalone-chrome'
      sh 'docker exec seleniumenv python test.py'
      }
    }
  }
  post {
        always {
            // Stop and remove all containers
            sh 'docker stop $(docker ps -a -q)'
sh 'docker rm $(docker ps -a -q)'
sh 'docker rmi $(docker images -a -q)'
sh 'docker network rm ml_network'
        }
    }
}
