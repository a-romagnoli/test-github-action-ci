pipeline {
    agent { docker { image 'python:3.9' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m pip install --upgrade pip'
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
