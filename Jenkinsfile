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
                    sudo pkill -f "python app.py" || true
                    . venv/bin/activate
                    nohup python app.py > flask.log 2>&1 &
                '''
                sleep time: 50, unit: 'SECONDS'
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
