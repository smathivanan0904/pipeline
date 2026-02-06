pipeline {
 agent any
 stages {
 stage('Checkout Code') {
 steps {
 git 'https://github.com/your-username/your-repo.git'
 }
 }
 stage('Create File') {
 steps {
 bat 'echo This file is created by Jenkins > demo.txt'
 }
 }
 }
}
