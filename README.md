# doccollect

The docker container deploys two apps: brat and doccollect.
Brat is accessible at localhost:9000, and doccollect is accessible at localhost:9001.

Doccollect exposes a list of all uploaded documents at localhost:9001/docs
and a form to upload documents at localhost:9001/docs/create.

Once PDFs have been submitted through doccollect, they become
available for annotation at brat in the doccollect directory.

Users need to login to brat to be allowed to create annotations.
The username and password are the ones specified when launching the docker container.

See [brat.md](brat.md) for more information.
