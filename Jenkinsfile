pipeline {
    agent any

    stages {
      
        stage('Checkout') {
            steps {
                // Checkout the code from your Git repository
                checkout scm
            }
        }
        

        stage('Run Tests') {
            steps {
                // Run your Selenium tests
                sh 'python test.py'
            }
        }
    }
}
