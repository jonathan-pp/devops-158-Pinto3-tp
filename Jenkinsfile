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

        stage('Pull latest code') {
            steps {
                dir('/root/devops-158-Pinto3-tp/') {
                    git branch: 'main', url: 'https://github.com/jonathan-pp/devops-158-Pinto3-tp.git'
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
            echo 'Déploiement automatique réussi ! BRAVO DAMN'
        }
        failure {
            echo 'Échec du pipeline. - AIE AIE AIE CA PUE'
        }
    }
}
