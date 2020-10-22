pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh 'python3 test_main.py'
      }
    }
    stage('Build') {
      steps {
        sh 'python3 main.py'
      }   
    }
	stage('Package') {
      steps {
        sh 'tar -cvzf calculator.tar.gz *'
      }   
    }
  }
}