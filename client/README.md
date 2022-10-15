# Configure

Edit the `.env.production` file, and give the wanted values.

# Build

```shell
docker-compose run --rm client yarn build
```

# Start

```shell
cd dist
docker-compose up -d
```
