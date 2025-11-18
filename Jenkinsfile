pipeline {
    agent any
    
    // 1. Parameters Block (Inputs you give before the build starts)
    parameters {
        // String input
        string(name: 'VERSION_TAG', defaultValue: '', description: 'Manual version tag')
        
        // Dropdown choice input
        choice(name: 'VERSION_CHOICE', choices: ['1.1.0', '1.2.0', '1.3.0'], description: 'Select version')
        
        // Boolean checkbox (True/False)
        booleanParam(name: 'executeTests', defaultValue: true, description: 'Uncheck to skip tests')
    }

    environment {
        NEW_VERSION = '1.3.0'
    }
    
    stages {
        stage('Build') {
            steps {
                echo "Building version ${NEW_VERSION} on Windows..."
                echo "User selected choice: ${params.VERSION_CHOICE}"
                
                // Maven command removed as requested
                bat 'dir' 
            }
        }

        stage('Test') {
            // 2. The 'when' block determines if this stage runs
            when {
                expression { return params.executeTests }
            }
            steps {
                echo 'Testing Project...'
                echo 'This only runs if the checkbox was checked!'
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
