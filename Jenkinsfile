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
stage('Post') {
always {
echo 'Post build condition running'    
}
failure {
echo 'Post action if build failed'    
}

}
}
