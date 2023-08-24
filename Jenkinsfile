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

    post {
        always {
            // Archive the JUnit XML report as a build artifact
            archiveArtifacts artifacts: 'test-reports/**/*.xml', allowEmptyArchive: true

            // Publish JUnit test results using the Jenkins JUnit Plugin
            junit 'test-reports/**/*.xml'
        }
    }
}
