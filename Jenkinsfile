pipeline {
    agent any
    stages {
        stage('MongoDB Setup') {
            steps {
                script {
                    try {
                        sh 'docker stop mongo_unittest'
                        sh 'docker rm mongo_unittest'
                    } catch (err) {
                        echo 'docker mongo_unittest is not already running' // err.getMessage()
                    }
                }
                sh 'docker pull mongo:4'
                sh 'docker run -d --name mongo_unittest -p 27017:27017 mongo:4'
            }
        }
        stage('Run Flask Unittests') {
            agent {
                docker {
                    image 'python:3.9'
                    args '--user 0:0 --net host'
                }
            }
            steps {
                checkout scm
                sh 'pip install -r requirements.txt'
                sh 'pip install -e .'
                sh 'echo "MONGO_HOST=127.0.0.1" >> web/.env'
                sh 'coverage run web/test/main.py'
            }
            post {
                always {
                    sh 'coverage report'
                }
            }
        }
    }
    post {
        always {
            sh 'docker stop mongo_unittest'
            sh 'docker rm mongo_unittest'
        }
    }
}
