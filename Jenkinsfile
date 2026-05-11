pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jonathan-pp/devops-158-Pinto3-tp'
            }
        }

        stage('Pull latest code') {
            steps {
                dir('/root/devops-158-Pinto3-tp/') {
                    git branch: 'main', url: 'https://github.com/jonathan-pp/devops-158-Pinto3-tp'
                }
            }
        }

        stage('Install dependencies') {
            steps {
                dir('/root/devops-158-Pinto3-tp/') {
                    sh '''
                        . venv/bin/activate
                        pip install flask pytest
                    '''
                }
            }
        }

        stage('Run unit tests') {
            steps {
                dir('/root/devops-158-Pinto3-tp/') {
                    sh '''
                        . venv/bin/activate
                        python -m pytest test_app.py -v --tb=short
                    '''
                }
            }
        }

        stage('Restart Flask app') {
            steps {
                sh '''
                    pkill -f "python app.py" || true
                    cd /root/devops-158-Pinto3-tp/
                    . venv/bin/activate
                    nohup python app.py > flask.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo 'Deploiement automatique reussi ! BRAVO DAMN'
        }
        failure {
            echo 'echec du pipeline. - AIE AIE AIE CA PUE'
        }
    }
}éééééééé
