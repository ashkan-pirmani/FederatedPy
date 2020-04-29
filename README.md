Docker Container to Help Custodians
-----------
#DataSavesLives – #MSCOVID19

As the COVID-19 pandemic unfolds across the globe, the demand for data on the impact of the novel coronavirus on people with Multiple Sclerosis (MS) grows rapidly.
This information is crucial for people with MS and clinicians to make evidence-based decisions on how to manage their condition during the pandemic or in case of a COVID-19 infection.
MS Data Alliance and the MS International Federation have teamed up to set up a Global Data Sharing Initiative and are calling for individuals and organisations across the global MS movement to get involved.  Watch our animation.

Install Docker Desktop on Mac
-----------
You can easily download the Docker for Mac by clicking on this Link!

https://hub.docker.com/editions/community/docker-ce-desktop-mac/

System requirements For Mac
---------

Your Mac must meet the following requirements to successfully install Docker Desktop:

Mac hardware must be a 2010 or a newer model, with Intel’s hardware support for memory management unit (MMU) virtualization, including Extended Page Tables (EPT) and Unrestricted Mode. You can check to see if your machine has this support by running the following command in a terminal: sysctl kern.hv_support

If your Mac supports the Hypervisor framework, the command prints kern.hv_support: 1.

macOS must be version 10.13 or newer. That is, Catalina, Mojave, or High Sierra. We recommend upgrading to the latest version of macOS.

If you experience any issues after upgrading your macOS to version 10.15, you must install the latest version of Docker Desktop to be compatible with this version of macOS.

Note: Docker supports Docker Desktop on the most recent versions of macOS. That is, the current release of macOS and the previous two releases. Docker Desktop currently supports macOS Catalina, macOS Mojave, and macOS High Sierra.

As new major versions of macOS are made generally available, Docker stops supporting the oldest version and support the newest version of macOS (in addition to the previous two releases).

At least 4 GB of RAM.

VirtualBox prior to version 4.3.30 must not be installed as it is not compatible with Docker Desktop.




Install Docker Desktop on Windows
-----------

System requirements For Windows
---------

Windows 10 64-bit: Pro, Enterprise, or Education (Build 15063 or later).
Hyper-V and Containers Windows features must be enabled.
The following hardware prerequisites are required to successfully run Client Hyper-V on Windows 10:

64 bit processor with Second Level Address Translation (SLAT)
4GB system RAM
BIOS-level hardware virtualization support must be enabled in the BIOS settings. For more information, see Virtualization.



Docker Desktop for Windows is the Community version of Docker for Microsoft Windows. You can download Docker Desktop for Windows from Docker Hub.

https://hub.docker.com/editions/community/docker-ce-desktop-windows/




Check versions
------------

Ensure your versions of docker and docker-compose are up-to-date and compatible with Docker.app. Your output may differ if you are running different versions.

```
$ docker --version
Docker version 19.03, build c97c6d6
```


Build
-----------
Pull the latest Docker Image ( you can find the command in the docker page)

```
docker pull ashkanpirmani/federated-py
```

Run
-----------
By entering the following command in the terminal/cmd you can easily run the docker engine with python
```
docker run ashkanpirmani/federated-py
```