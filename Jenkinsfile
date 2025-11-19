pipeline {
    agent any

    environment {
        // SonarQube Tool Names (from your Jenkins configuration)
        SONAR_SCANNER_NAME = 'sonar_scanner'
        SONAR_SERVER_NAME = 'SonarQube'

        // SonarQube Project Identification (DEFINE YOUR OWN VALUES HERE)
        SONAR_PROJECT_KEY  = 'ssd-lab12'
        SONAR_PROJECT_NAME = 'ssd flask app lab12'

        // Existing variable (kept for context)
        NEW_VERSION = '1.3.0'
    }

    stages {
        stage('Build') {
            steps {
                echo "Building version ${NEW_VERSION} on Windows..."
                // Replace this with your actual build command (e.g., Maven, Gradle)
                bat 'echo Running Build Step...'
            }
        }

        stage('SonarQube Analysis') {
            // The withSonarQubeEnv step securely passes the server URL and token
            withSonarQubeEnv(SONAR_SERVER_NAME) {
                steps {
                    echo "Starting SonarQube Analysis for project ${env.SONAR_PROJECT_NAME}..."
                    
                    // Execute the SonarScanner tool using the configured tool name.
                    // The properties define the key and name in SonarQube.
                    bat "${SONAR_SCANNER_NAME}\\bin\\sonar-scanner " + 
                        "-Dsonar.projectKey=${SONAR_PROJECT_KEY} " + 
                        "-Dsonar.projectName=${SONAR_PROJECT_NAME} " + 
                        "-Dsonar.sources=." 
                }
            }
        }

        stage('Quality Gate Check') {
            // Wait for the analysis report to be processed by SonarQube.
            steps {
                timeout(time: 30, unit: 'MINUTES') {
                    // This step polls the SonarQube server and fails the Jenkins build
                    // if the project fails its Quality Gate.
                    script {
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            error "Pipeline failed due to SonarQube Quality Gate failure: ${qg.status}"
                        }
                    }
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Testing Project...'
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
