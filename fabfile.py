from fabric.api import cd, run, env

env.hosts = ['pi@192.168.1.57']

def deploy():
    print('Deploying master...')
    with cd('/home/pi/poppins'):
        run('git pull origin master')

def restart():
    print('Restarting...')
    run('sudo restart poppins')