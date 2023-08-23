pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your Git repository
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                // Set up environment (install dependencies, etc.)
                sh 'pip install -r requirements.txt' // Install Python dependencies
            }
        }

        stage('Run Tests') {
            steps {
                // Run your Selenium tests
                sh 'python3 test.py'
            }
        }
    }
}
