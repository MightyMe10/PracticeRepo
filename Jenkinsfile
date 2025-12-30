pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }
        
        stage('Build') {
            steps {
                bat 'powershell -ExecutionPolicy Bypass -File build.ps1'
            }
        }
        
        stage('Deploy') {
            steps {
                bat 'powershell -ExecutionPolicy Bypass -File deploy.ps1'
            }
        }
    }
}
