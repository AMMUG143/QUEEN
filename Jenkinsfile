pipeline{
    agents any

    stages{
        stage('Checkout Code'){
            steps{
                git url :'https://github.com/AMMUG143/WORLD.git' , branch: 'main'
            }
        }
    
        stage('Install Dependencies'){
            steps{
                bat '''
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install pytest
                '''
            }
        }

        stage('Run Tests'){
            steps{
                bat '''
                    call venv\\Scripts\\activate
                    pytest hlo.py
                '''
            }
        }


        stage('deploy'){
            steps{
                echo 'Deploying to Application...'
                bat '''
                    call venv\\Scripts\\activate
                    python test.py
                '''
            }
        }
    }
}
             
