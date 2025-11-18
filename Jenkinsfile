pipeline {
    agent any
    
    // 1. The 'tools' block tells Jenkins to auto-install/use specific software.
    // The name 'Maven3' MUST match what you configure in step 2 below.
    tools {
        maven 'Maven3' 
    }

    environment {
        NEW_VERSION = '1.3.0'
    }
    
    stages {
        stage('Build') {
            steps {
                echo "Building version ${NEW_VERSION} on Windows..."
                
                // 2. Use 'bat' for Windows (Linux uses 'sh')
                // 'mvn clean install' compiles the code and packages it
                bat 'mvn clean install' 
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Example: bat 'mvn test'
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
