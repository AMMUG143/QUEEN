pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/AMMUG143/WORLD.git', branch: 'main'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                bat '''
                    echo Creating virtual environment...
                    python -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    echo Running tests...
                    pytest hlo.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    echo Deploying app...
                    python test.py
                '''
            }
        }
    }
}

      
