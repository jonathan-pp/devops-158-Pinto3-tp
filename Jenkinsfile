pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install flask
                '''
            }
        }

        stage('Restart Flask app') {
            steps {
                sh '''
                    # Essayer plusieurs patterns
                    pkill -f "app.py" || true
                    pkill -f "flask" || true
                    # Attendre que le port soit libéré
                    sleep 2
                    export JENKINS_NODE_COOKIE=dontKillMe
                    . venv/bin/activate
                    nohup python app.py > flask.log 2>&1 &
                    echo $! > flask.pid
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
