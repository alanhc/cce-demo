CCE-demo
===

## Links

[TOC]

## Beginners Guide

If you are a total beginner to this, start here!

1. Download [git](https://git-scm.com/downloads)
2. Clone this project `git clone https://github.com/alanhc/cce-demo.git`
3. Complete pre-requirements 
```shell
cd frontend
pip install -r requirements.txt
```
3. Run `python main.py`
4. Start!


Control flows
---
```sequence
client->server: POST method {file:byteImage}
server->client: streamingResponse(image/png)
```
