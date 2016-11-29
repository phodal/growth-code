node {

  stage ('Checkout') {
    git 'https://github.com/phodal/growth-studio'
  }

  stage ('Create Virtualenv') {
    sh './ci/setup.sh'
  }

  stage ('Install') {
    sh './ci/install.sh'
  }

  stage ('Unit Test') {
    sh './ci/unit_test.sh'
  }

  stage ('E2E Test') {
    sh './ci/e2e.sh'
  }
  
  stage ('Deploy') {
    sh './ci/deploy.sh'
  }
}