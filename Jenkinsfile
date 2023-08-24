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
                sh 'pip install -r requirements.txt --junitxml=test-reports/results.xml' // Install Python dependencies
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 test.py'
            }
        }

        stage('Generate Allure Reports') {
            steps {
                sh 'allure generate allure-results --clean -o allure-report'
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
