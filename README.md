# Personal Project: Working with Ignition Locally using Docker

This repository contains a personal project demonstrating how to set up and work with Ignition locally using Docker. Below are the steps and commands to get started.

## Prerequisites

Make sure you have the following installed on your system:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Steps to Use

### Inspect Docker Network

To inspect the network used by the project:

```bash
docker network inspect ignition_my_network
```

### Build Modbus Simulator

To build the Modbus simulator service:

```bash
docker-compose build modbus-simulator
```

## Notes

- Replace `ignition_my_network` with your actual network name if different.
- Ensure all dependencies and configurations are properly set up in the `docker-compose.yml` file.

---

Feel free to contribute or use this project as a reference for your own Docker-based Ignition setups!
