pipeline {
    agent any

    tools {
        nodejs 'NodeJS' // Make sure you have a NodeJS tool configured in Jenkins with this name
    }

    stages {
        stage('Install Dependencies') {
            steps {
                /*
                 * Install dependencies.
                 * On Windows agents, 'sh' might fail if Git Bash isn't in PATH.
                 * Use 'bat' for Windows batch commands.
                 */
                bat 'npm install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'npm test'
            }
        }

        stage('Build Docker Image') {
            // Only run this stage if you have Docker installed
            steps {
                script {
                   echo 'Building Docker image...'
                   // bat 'docker build -t my-jenkins-app .'
                   echo 'Docker build skipped. Uncomment the line above if Docker is installed.'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
