from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .DockerManager import DockerManager
from .NGINXConfigurator import NGINXConfigurator
from .models import Profile, Session
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.conf import settings
from django.contrib.sessions.models import Session as DjangoSession


def get_sessions_data():
    return tuple((session.user.volume, session.port, session.sessionid)
                 for session in Session.objects.all())


@receiver(post_save, sender=Profile)
def profile_saved(sender, instance, **kwargs):
    # Check if volume already exists and if not -> creating new volume
    if instance.volume is None:
        docker_manager = DockerManager()
        volume = docker_manager.create_new_volume(instance.username)
        instance.volume = volume

        instance.save()


@receiver(user_logged_in)
def profile_start_up(sender, user, request, **kwargs):
    try:
        user.session
        user.session.sessionid = request.session.session_key
        user.session.save()
    except Profile.session.RelatedObjectDoesNotExist:
        # Create session
        session = Session()
        session.user = user
        session.sessionid = request.session.session_key

        # Create container
        docker_manager = DockerManager()

        # Port range
        port = settings.AVAILABLE_PORTS_RANGE[0]
        container_id = -1
        while True:
            try:
                container_id = docker_manager.turn_on_container(user.volume,
                                                                port)
                break
                # TODO dodać konkret bledy
            except:
                port += 1

        session.port = port
        session.container_id = container_id
        session.save()
    finally:
        NGINXConfigurator.refresh_config(get_sessions_data())


@receiver(pre_delete, sender=DjangoSession)
def close_session(sender, instance, **kwargs):
    # Obtaining container_id
    try:
        session = Session.objects.get(sessionid=instance.session_key)
        container_id = session.container_id

        # Turn off and delete container
        docker_manager = DockerManager()
        docker_manager.turn_off_container(container_id)

        # Delete session
        session.delete()
        print("Closed session!")
    except Session.DoesNotExist:
        pass
    NGINXConfigurator.refresh_config(get_sessions_data())


@receiver(pre_delete, sender=Profile)
def clean_up_volume(sender, instance, **kwargs):
    try:
        volume_id = instance.volume

        docker_manager = DockerManager()
        docker_manager.remove_volume(volume_id)

    except :
        pass
