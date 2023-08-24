pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                sh 'pip install -r requirements.txt' // Install Python dependencies
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 test.py'
            }
        }

    }

}
