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
                sh 'python3 -m pip install google-cloud-storage google-cloud-bigquery pytest'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                export PATH=$PATH:/Users/shixiaotong/Library/Python/3.9/bin
                pytest tests/
                '''
            }
        }

        stage('Debug Authentication') {
            steps {
                sh '''
                export PATH=$PATH:/Users/shixiaotong/google-cloud-sdk/bin/
                gcloud auth activate-service-account --key-file=$GCP_KEY_FILE
                gcloud auth list
                '''
            }
        }

        stage('Deploy Pipeline') {
            steps {
                sh '''
                python3 pipeline.py
                '''
            }
        }
    }
}
