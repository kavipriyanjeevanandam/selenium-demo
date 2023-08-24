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
                    . /var/jenkins_home/venv/bin/activate
                    pip install -r requirements.txt
                '''
                
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
