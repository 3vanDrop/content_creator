pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                echo 'Simulando clonación de repositorio (No es necesario en este ejemplo)'
            }
        }
        stage('Set up Python Environment') {
            steps {
                sh '''
                python3 -m venv env
                source env/bin/activate
                pip install -r requirements.txt || echo "No hay dependencias para instalar"
                '''
            }
        }
        stage('Run Python Script') {
            steps {
                sh '''
                source env/bin/activate
                python3 script.py
                '''
            }
        }
    }
}
