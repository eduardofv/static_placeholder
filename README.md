# static-placeholder

A minimal "coming soon" placeholder page served by Python inside a Docker container.

## Files

| File | Purpose |
|------|---------|
| `index.html` | Single-page placeholder |
| `serve.py` | Python HTTP server (logs every request) |
| `Dockerfile` | Container definition |

## Build

```bash
docker build -t placeholder .
```

## Run

Port is set via a command-line argument or the `PORT` environment variable. Default is `8080`.

```bash
# argument
docker run -p 9000:9000 placeholder 9000

# environment variable
docker run -e PORT=9000 -p 9000:9000 placeholder

# default port 8080
docker run -p 8080:8080 placeholder
```

The server binds to `0.0.0.0` and logs every request to stdout:

```
Serving on 0.0.0.0:9000
172.17.0.1 - [02/May/2026 18:00:00] "GET / HTTP/1.1" 200 -
```

View live logs from a running container:

```bash
docker logs -f <container-id>
```
