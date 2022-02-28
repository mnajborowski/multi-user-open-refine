import subprocess


class NGINXConfigurator:
    _config_path = "/etc/nginx/conf.d/muor.conf"
    _location_preamble_path = "MUOR/configs/muor_before_location_block.conf"
    _location_epilouge_path = "MUOR/configs/muor_after_location_block.conf"

    @classmethod
    def refresh_config(cls, sessions):
        """
        Expects sessions in form of tuple of (uid, port, sessionid) entries.
        """
        config = cls._get_config(sessions)
        with open(cls._config_path, 'w') as F:
            F.write(config)
        completed_process = subprocess.run(
            ["sudo", "/usr/sbin/service", "nginx", "reload"])
        return completed_process.returncode

    @classmethod
    def _get_config(cls, sessions):
        config = "\n".join(
            cls._get_upstream_entry(uid, port) for uid, port, sessionid in
            sessions)
        config += cls._get_locations_preamble()
        config += "\n".join(
            cls._get_location_entry(uid, sessionid) for uid, port, sessionid in
            sessions)
        config += cls._get_locations_epilogue()

        return config

    @classmethod
    def _get_locations_preamble(cls):
        with open(cls._location_preamble_path) as F:
            return F.read()

    @classmethod
    def _get_locations_epilogue(cls):
        with open(cls._location_epilouge_path) as F:
            return F.read()

    @classmethod
    def _get_upstream_entry(cls, uid, port):
        return f"upstream {uid}" + " {\n" \
               + f"    server localhost:{port};" + "\n}"

    @classmethod
    def _get_location_entry(cls, uid, sessionid):
        return f'if ($cookie_sessionid = "{sessionid})"' + " {\n" \
               + f"proxy_pass http://{uid};" + "\n}"
