pipeline {


agent any

stages {

    stage('Install Dependencies') {

        steps {

            sh '''
            python3 -m pip install --upgrade pip
            python3 -m pip install -r requirements.txt
            '''
        }
    }

    stage('Run Pytest Automation') {

        steps {

            sh '''
            pytest test_cases/ --browser chrome --headless
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
