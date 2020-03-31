def api_job_id = 'UNKOWN'

pipeline {
    agent any
    stages {
        stage('Initialize') {
            agent { label "${LABEL_SET}" }
            steps {
                script {
                    api_job_id = sh(returnStdout: true, script: '/usr/lab_auto/create_job.py --plan_id ${PLAN_ID} --type "${PLAN_TYPE}" --url "BUILD_URL"')
                    api_job_id = api_job_id.trim()
                    echo "API Job ID: [${api_job_id}]"
                }
            }
        }
        stage('Lanuch Tests') {
            parallel {
                stage('T1') {
                    agent { label "${LABEL_SET}" }
                    steps {
                        sh "sudo python3 /usr/lab_auto/run_task.py -v -j ${api_job_id} -t 2058"
                    }
                }
                stage('T2') {
                    agent { label "${LABEL_SET}" }
                    steps {
                        sh "sudo python3 /usr/lab_auto/run_task.py -v -j ${api_job_id} -t 2057"
                    }
                }
            }
        }
    }
}