pipeline {
    agent any

    // 1. Define environment variables here
    environment {
        NEW_VERSION = '1.3.0'
    }
    
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                
                // 2. Using the variable. 
                // IMPORTANT: You must use double quotes " " for variables to work.
                echo "Building version ${NEW_VERSION}" 
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
    
    post { 
        always {
            echo 'Post build condition running'   
        }
        failure {
            echo 'Post action if build failed'   
        }
    }
}
