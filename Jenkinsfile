pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jonathan-pp/devops-158-Pinto3-tp.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install flask pytest
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m pytest app.py -v --tb=short
                '''
            }
        }
    }
}
