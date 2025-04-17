pipeline {
    agent any

    stages{
        stage('Checkout Code'){
            steps{
                git url :'https://github.com/AMMUG143/WORLD.git' , branch: 'main'
            }
        }
    
        stage('Install Dependencies'){
            steps{
                bat '''
                    C:\\Users\\amrutha\\AppData\\Local\\Programs\\Python\\Python313\\python.exe
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
                    pytest test.py
                '''
            }
        }


        stage('deploy'){
            steps{
                echo 'Deploying to Application...'
                bat '''
                    call venv\\Scripts\\activate
                    C:\\Users\\amrutha\\AppData\\Local\\Programs\\Python\\Python313\\python.exe
                '''
            }
        }
    }
}


        
