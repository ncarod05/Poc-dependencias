pipeline {
    agent any

    environment {
        DEPLOY_DIR = "/opt/app-deploy"
        VENV_NAME = "venv"
    }

    stages {
        stage('1. Dependency Management') {
            steps {
                echo "==> [Jenkins Manual] Verificando requirements.txt..."
                sh '''
                    if [ ! -f "requirements.txt" ]; then
                        echo "Error: No se encontró el archivo requirements.txt en el repositorio"
                        exit 1
                    fi
                    cat requirements.txt
                '''
            }
        }

        stage('2. Build') {
            steps {
                echo "==> [Jenkins Manual] Configurando entorno virtual e instalando dependencias..."
                sh '''
                    python3 -m venv ${VENV_NAME}
                    . ${VENV_NAME}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('3. Test') {
            steps {
                echo "==> [Jenkins Manual] [TEST] Aquí se simulan las pruebas unitarias..."
                sh 'echo "Pruebas superadas con éxito en el workspace de Jenkins."'
            }
        }

        stage('4. Deploy (Simulado)') {
            steps {
                echo "==> [Jenkins Manual] Desplegando en la máquina Kali Linux..."
                sh '''
                    sudo mkdir -p ${DEPLOY_DIR}
                    sudo cp app.py requirements.txt ${DEPLOY_DIR}/
                    echo "¡Despliegue manual desde Jenkins completado en ${DEPLOY_DIR}!"
                '''
            }
        }
    }

    post {
        success {
            echo "¡El build manual finalizó correctamente!"
        }
        failure {
            echo "El pipeline falló durante la ejecución manual."
        }
    }
}
