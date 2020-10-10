# Troubleshooting

Tips from the dev team

## Clean start

If you want/need a clean state you can delete the var docker volume.
`docker volume rm var-gemeindescan-webui`

## Visual Studio Code

If you have a vscode related problem it could help to delete the vscode docker volume.
- django: `docker volume rm gemeindescan-webui_vscode-remote-django`
- vue: `docker volume rm gemeindescan-webui_vscode-remote-vue`

## Django

When the `./manage.py` doesn't work your need to execute `python3 manage.py` instead.

## Docker

Do a `docker-compose kill` and `docker-compose rm` if there are some container problems.

With `docker-compose logs -f` you can see the output of the containers if there is a problem.

### docker cleanup

If you are sure that you want to clean up your entire Docker environment, run `docker system prune` and follow the prompts.

Alternatively, with `docker images` you can list all download images and display the hash image id.
Do `docker rmi 2dadea35c9d0 8ae2cb92062c ...` to delete not needed images and free up some space.

### docker cgroups

If you get an error like `Cannot start service www: cgroups: cgroup mountpoint does not exist: unknown`, then your Linux kernel is probably configured for newer container systems. Check out [this article](https://poweruser.blog/how-to-install-docker-on-fedora-32-f2606c6934f1), and for Fedora users in particular the instruction `sudo grubby --update-kernel=ALL --args="systemd.unified_cgroup_hierarchy=0"`.

## Database

If you get an error like `Host is unreachable. Is the server running on host "pdb" and accepting TCP/IP connections on port 5432?`, check the logs from the pdb container. If it contains `database files are incompatible with server`, run this command:

`make update-db`

And if all else fails, `make drop-db` and `make init` again.
