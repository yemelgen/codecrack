# Native API

This is a functional example of how to expose functions written in C to a Vue.js frontend.

Before one of my technical interviews, I was informed that I might be asked about integrating low-level C code into a modern web application. Rather than just reading up on it, I decided to build a working example from scratch to better understand the full flow — and to be well-prepared.

## Installation

First, you need to set up python environment. Make sure that you use Python 3.6 or higher:
```console
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

Then, build binaries:
```console

make -C core
mv core/libsecret.x64.so backend
```

Lastly, launch the backend:
```console
python backend/main.py
```

Now, you should be able to use the frontend:
```console
google-chrome frontend/index.html
```
Enjoy :)
