import docker
import hashlib
from django.conf import settings


class DockerManager:
    def __init__(self):
        self.client = docker.from_env()
        self.image = settings.DOCKER_IMAGE

    def create_new_volume(self, username):
        # Hashing username to get volume name
        hashed_username = hashlib.sha256(bytes(username, 'utf-8')).hexdigest()

        # Creating volume in docker
        volume = self.client.volumes.create(name=hashed_username, driver='local')

        return volume.id

    def turn_on_container(self, volume_id, port):
        container = self.client.containers.run(self.image, detach=True,
                                               volumes={volume_id: {"bind": "/data", "mode": "rw"}},
                                               ports={'3333': port})
        return container.id

    def turn_off_container(self, container_id):
        container = self.client.containers.get(container_id)
        container.stop()
        container.remove()

    def remove_volume(self, volume_id):

        volume = self.client.volumes.get(volume_id)

        if volume is not None:
            volume.remove(force=True)

