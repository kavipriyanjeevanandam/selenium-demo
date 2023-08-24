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
                 // Activate the virtual environment
                sh '''
                    source /var/jenkins_home/venv/bin/activate
                '''
                sh 'pip install -r requirements.txt' // Install Python dependencies
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 test.py'
                sh '''
                    deactivate
                '''
            }
        }

    }

}
