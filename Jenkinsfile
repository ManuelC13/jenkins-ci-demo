pipeline {
    agent any

    stages {

        stage('1. Preparar entorno') {
            steps {
                echo 'Creando entorno virtual...'
                sh 'python3 -m venv .venv'
            }
        }

        stage('2. Instalar dependencias') {
            steps {
                echo 'Instalando dependencias...'
                sh '.venv/bin/pip install pytest'
            }
        }

        stage('3. Ejecutar pruebas') {
            steps {
                echo 'Ejecutando pruebas automatizadas...'
                sh '.venv/bin/pytest tests/test_calculadora.py -v'
            }
        }

        stage('4. Build listo') {
            steps {
                echo 'El proyecto está listo para ser desplegado (fase de CD)'
            }
        }

    }

    post {
        success { 
            echo 'Pipeline exitoso: el código es estable y está listo para entrega.'
        }
        failure { 
            echo 'Pipeline fallido: corregir errores antes de integrar cambios.'
        }
    }
}
