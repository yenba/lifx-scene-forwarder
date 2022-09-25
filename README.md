# **lifx-scene-forwarder**

This is a docker container that when run, will launch a local API web server that allows you to kick off LIFX scenes by just using the Scene Name in a GET request. 

For example, if you have a LIFX Scene named `Good Morning` you would be able to kick off that scene easily by just browsing too or making a GET request to the following URL:

```bash
http://localhost:8088/scenes/GoodMorning
```

The reason I built this is to easily kick off LIFX Scenes from within SmartThings, utilizing toddaustin07’s wonderful SmartThings Edge Driver, https://github.com/toddaustin07/webrequestor.

This way I no longer need to add a body and headers to my HTTP Requests from within SmartThings, instead just a simple URL with the LIFX Scene Name.

## Prerequisites

- **LIFX API Key**
    - Generate a LIFX Personal Access Token at the following URL: [https://cloud.lifx.com/settings](https://cloud.lifx.com/settings)
- **Docker & Docker Compose**

## Instructions

Clone this git repo:

```bash
git clone https://github.com/yenba/lifx-scene-forwarder.git
```

Go into the folder:

```bash
cd lifx-scene-forwarder
```

Modify the `config/lifxconfig.cfg` file and replace the placeholder API key with your own:

```bash
nano config/lifxconfig.cfg
```

Run the `docker-compose.yml` file:

```bash
docker-compose up -d
```

Once the docker container is downloaded and ran, the web server should be up and running at [http://localhost:8088/](http://localhost:8088/). You can verify this by going to [http://localhost:8088/](http://localhost:8088/) in a web browser and you should see the following result in your browser:

```bash
{"Hello":"World"}
```

You’re now ready to run LIFX scenes! The format is shown below:

```bash
http://localhost:8088/scenes/LIFX_SCENE_NAME_HERE
```

**⚠️ Note: You need to make sure you remove all spaces from your LIFX Scene Name.** ⚠️

For example, if your scene in LIFX is named `Good Morning` you would need to change that to `GoodMorning` and your URL would look like this:

```bash
http://localhost:8088/scenes/GoodMorning
```

**Enjoy!**
