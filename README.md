# DocuBot

1. run `./traverse.sh` in the directory with source code you seek to generate documentation for and copy the contents into ./file.txt.

2. run `./generate-prompts.sh`

3. run `docker run -it -v /path/to/docubot/:/app/ -u $(id -u):$(id -g) docubot`