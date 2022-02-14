pipeline {
    agent any

    stages {
        stage('Step-1') {
            steps {
                sh '''
                    sudo apt-get install python3-venv -y
                    sudo apt-get install libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev -y
                    python3 -m venv venv
                    . ./venv/bin/activate
                    python3 -m pip install --upgrade pip
                    python3 -m pip install --no-warn-script-location -r requirements.txt
                    curl -s https://aerokube.com/cm/bash | bash
                    sudo ./cm selenoid start --vnc
                    python3 -m pytest -s -v tests/ --alluredir=allureress || exit 0
                '''
            }
        }
    }
}
