pipeline {
 agent any
 stages {
 stage('Checkout Code') {
 steps {
 git 'https://github.com/smathivanan0904/pipeline.git'
 }
 }
 stage('Read File') {
 steps {
 bat 'type README.md'
 }
 }
 }
}
