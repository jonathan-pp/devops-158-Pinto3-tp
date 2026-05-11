pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

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

        stage('Run unit tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m pytest test_app.py -v --tb=short
                '''
            }
        }

        stage('Restart Flask app') {
            steps {
                sh '''
                    pkill -f "python app.py" || true
                    . venv/bin/activate
                    nohup python app.py > flask.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo 'Déploiement automatique réussi ! BRAVO DAMN'
        }
        failure {
            echo 'Échec du pipeline. - AIE AIE AIE CA PUE'
        }
    }
}pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jonathan-pp/devops-158-Pinto3-tp.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install flask pytest
                '''
            }
        }

        stage('Run unit tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m pytest test_app.py -v --tb=short
                '''
            }
        }

        stage('Restart Flask app') {
            steps {
                sh '''
                    pkill -f "python app.py" || true
                    . venv/bin/activate
                    nohup python app.py > flask.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo 'Déploiement automatique réussi ! BRAVO DAMN'
        }
        failure {
            echo 'Échec du pipeline. - AIE AIE AIE CA PUE'
        }
    }
}
