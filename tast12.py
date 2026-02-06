pipeline {
 agent any
 stages {
 stage('Checkout Code') {
 steps {
 git 'https://github.com/your-username/your-repo.git'
 }
 }
 stage('Print Directory') {
 steps {
 bat 'cd'
 }
 }
 }
}
