FROM python:3.10-alpine3.19

COPY requirements.txt /temp/requirements.txt

COPY runapp /runapp
WORKDIR /runapp
EXPOSE 8000

#RUN #podman run -p 9000:9000 -p 9001:9001 minio/minio server /data --console-address ":9001"
RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password new-user
#RUN -p 127.0.0.1:16379:6379 --name redis-celery -d redis
USER new-user


#FROM node:20-slim AS base
#ENV PNPM_HOME="/pnpm"
#ENV PATH="$PNPM_HOME:$PATH"
#RUN corepack enable
#COPY . /app
#WORKDIR /app
#
#FROM base AS prod-deps
#RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --prod --frozen-lockfile
#
#FROM base AS build
#RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --frozen-lockfile
#RUN pnpm run build
#
#FROM base
#COPY --from=prod-deps /app/node_modules /app/node_modules
#COPY --from=build /app/dist /app/dist
#EXPOSE 8000
#CMD [ "pnpm", "start" ]