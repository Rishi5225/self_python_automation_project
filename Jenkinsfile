
from beginning and end.

---

# YOUR Jenkinsfile SHOULD LOOK EXACTLY LIKE THIS

:::writing{variant="document" id="54821"}
pipeline {

    agent any

    stages {

        stage('Clone Repository') {

            steps {

                git 'https://github.com/Rishi5225/self_python_automation_project.git'

            }
        }

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
:::

---

# THEN

Save file.

Then push again:

```bash id="k9m2q4"
git add .