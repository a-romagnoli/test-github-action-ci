pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '--user 0:0'
        }
    }
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install -e .'
                sh 'echo "MONGO_HOST=localhost" >> web/.env'
            }
        }
        stage('test') {
            steps {
                sh 'coverage run web/test/main.py'
            }
            post {
                always {sh 'coverage report'}
            }
        }
    }
}
