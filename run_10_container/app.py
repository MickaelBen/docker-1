import subprocess

DOCKER_COMMAND = "docker run -d -p"

container_name = 'bash'

port = 8000

nmb_container = 10

for i in range(nmb_container):
    full_docker_command = f"{DOCKER_COMMAND} {port}:8080 {container_name}"

    subprocess.run(full_docker_command, shell=True)

    port += 1
