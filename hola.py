pipeline {
    agent any  // Ejecuta en cualquier nodo disponible

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SofiaGal97/onejenk' 
            }
        }

        stage('Ejecutar Python') {
            steps {
                sh 'python hola.py' 
            }
        }
    }

    post {
        always {
            echo 'Pipeline completado.'
        }
    }
}