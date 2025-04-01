pipeline {
    agent any

    environment {
        GCP_KEY_FILE = credentials('gcp-service-account')  // Add this in Jenkins Credentials
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/XiaotongShi-create/jenkins-sandbox.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install google-cloud-storage google-cloud-bigquery'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Deploy Pipeline') {
            steps {
                sh """
                gcloud auth activate-service-account --key-file=$GCP_KEY_FILE
                python pipeline.py
                """
            }
        }
    }
}
