pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                // Here you can define commands for your build
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Here you can define commands for your tests
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                // Here you can define commands for your deployment
            }
        }
    }
    
    // The 'post' block defines actions to run at the end of the pipeline
    post { 
        always {
            echo 'Post build condition running - Always runs regardless of status'   
        }
        failure {
            echo 'Post action if build failed'   
        }
    }
}
