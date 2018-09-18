# Python 2.7

import logging
import json
import socket
import subprocess
import os

from httplib import HTTPConnection


STATE = dict(Yellow="PORT11=0:NC PORT12=128:NC PORT13=0:NC",
             Red="PORT11=0:NC PORT12=0:NC PORT13=128:NC",
             Green="PORT11=128:NC PORT12=0:NC PORT13=0:NC",
             Off="PORT11=0:NC PORT12=0:NC PORT13=0:NC",
             All="PORT11=128:NC PORT12=128:NC PORT13=128:NC")


def set_command(color):
    control_path = os.path.join(os.getcwd(), 'MP710.exe')
    cmd = "%s CMD=100 PRG=15 %s" % (control_path, STATE[color])
    p = subprocess.Popen(cmd, shell=True)
    p.wait()


if __name__ == "__main__":

    logging.basicConfig(filename='log_file.log', level=logging.DEBUG, filemode='w')

    set_command('Yellow')
    logging.debug("Start to validate...")

    try:
        connection = HTTPConnection('jenkins')
        connection.request("GET", "/api/main_build_status/")
        response = connection.getresponse()
        data = response.read()
        result = json.loads(data)

        BUILD_RESULT = result.get('build_status')
        TESTS_RESULT = result.get('functional_tests')
        ENV_RESULT = result.get('main_env_status')

        logging.debug("BUILD: %s" % BUILD_RESULT)
        logging.debug("TEST: %s" % TESTS_RESULT)
        logging.debug("ENV: %s" % ENV_RESULT)

        if BUILD_RESULT == "FAILED":
            set_command("Red")
            logging.debug("Build is FAILED")

        elif ENV_RESULT == "FAILED":
            set_command("Red")
            logging.debug("Env is FAILED")

        elif BUILD_RESULT == "STARTED":
            logging.debug("Build in progress")

        elif BUILD_RESULT == "SUCCESS":
            logging.debug("Build is OK.")

            if TESTS_RESULT == "SUCCESS":
                set_command("Green")
                logging.debug("Functional Tests are OK.")
            else:
                set_command("Red")
                logging.debug("Functional Tests are FAILED")

    except socket.error:
        set_command("Red")
        logging.debug("Some problem with internet!")
