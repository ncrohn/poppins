from fabric.api import run

HOSTS = ['pi@192.168.1.57']

def deploy():
    print('Deploying')
    run('ssh {%s} "cd /home/pi; git clone "'.format(HOSTS))
