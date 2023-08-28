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
                sh '''
                    . /var/jenkins_home/venv/bin/activate
                    python3 test.py
                    deactivate
                '''
            }
        }

    }

}
