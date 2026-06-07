pipeline {

    agent any

    stages {

        stage('Build Docker Image') {

            steps {

                sh '''
                docker build -t automation-framework:v1 .
                '''
            }
        }

        stage('Run Automation in Docker') {

            steps {

                sh '''
                docker run automation-framework:v1
                '''
            }
        }
    }

    post {

        always {

            echo 'Pipeline Execution Completed'
        }

        success {

            echo 'Automation Execution Passed'
        }

        failure {

            echo 'Automation Execution Failed'
        }
    }
}