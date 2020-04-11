#!/usr/bin/env groovy

pipeline {
    options {
      disableConcurrentBuilds()
      buildDiscarder(logRotator(numToKeepStr: '1'))
    }
    agent { label 'demo' }
    stages {
        stage('prepare build') {
            when {
                anyOf {
                    branch "development"
                }
            }
            steps {
                script {
                    env.nameSpace = "sharedservices"
                }
                checkout scm
                sh "git rev-parse --short HEAD > .git/commit-id"
            }
        }
        stage('QA: test prometheus') {
            when {
                anyOf {
                    branch "development"
                }
            }
            steps {
                script {
                    env.commit_id = readFile('.git/commit-id')
                }
                withCredentials([usernamePassword(credentialsId: 'k8s_cluster_pwd_qa', passwordVariable: 'k8s_pwd', usernameVariable: 'k8s_user')]) {
                    sh "echo test"
                }
            }
        }
        stage('QA: deploy prometheus') {
            when {
                anyOf {
                    branch "development"
                }
            }
            steps {
                script {
                    env.commit_id = readFile('.git/commit-id')
                }
                withCredentials([usernamePassword(credentialsId: 'k8s_cluster_pwd_qa', passwordVariable: 'k8s_pwd', usernameVariable: 'k8s_user')]) {
                    sh "kubectl create -f monitoring.yaml --namespace=sharedservices --server='https://k8s-master.demo.com' --username=${k8s_user} --password=${k8s_pwd} --insecure-skip-tls-verify=true"
                    sh "sleep 30"
                    sh "kubectl delete -f monitoring.yaml --namespace=sharedservices --server='https://k8s-master.demo.com' --username=${k8s_user} --password=${k8s_pwd} --insecure-skip-tls-verify=true"
                }
            }
        }
    }

}


@NonCPS
def static cleanBranchName(String branchName) {
    return branchName.replaceAll("/", "-")
}

@NonCPS
def getChangeString() {
    MAX_MSG_LEN = 100
    def changeString = ""

    echo "Gathering SCM changes"
    def changeLogSets = currentBuild.changeSets
    for (int i = 0; i < changeLogSets.size(); i++) {
        def entries = changeLogSets[i].items
        for (int j = 0; j < entries.length; j++) {
            def entry = entries[j]
            truncated_msg = entry.msg.take(MAX_MSG_LEN)
            changeString += " - ${truncated_msg} [${entry.author}]\n"
        }
    }

    if (!changeString) {
        changeString = " - No new changes"
    }
    return changeString
}
