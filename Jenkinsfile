pipeline {
    agent any

    stages {
        stage('Code Linting') {
            steps {
                echo 'Linting code...'
                sh 'echo "No linter configured."'
            }
        }
        stage('Build') {
            steps {
                echo 'Building app...'
                sh 'docker build -t myapp .'
            }
        }
        stage('Unit Test') {
            steps {
                echo 'Running unit tests...'
                sh 'echo "No unit tests configured."'
            }
        }
        stage('Deploy (Docker)') {
            steps {
                echo 'Deploying with Docker...'
                sh 'docker run -d -p 80:80 myapp'
            }
        }
        stage('Selenium Tests') {
            steps {
                echo 'Running Selenium tests...'
                sh 'docker build -f Dockerfile.selenium -t selenium-tests .'
                sh 'docker run selenium-tests'
            }
        }
    }
}
