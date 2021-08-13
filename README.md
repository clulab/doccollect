# doccollect

The docker container deploys two apps: brat and doccollect.
By default, brat is accessible at localhost:9002, and doccollect is accessible at localhost:9003.
(This is so that we can deploy on our server without remapping the ports.)

Doccollect exposes a list of all uploaded documents at localhost:9003/docs
and a form to upload documents at localhost:9003/docs/create.

Once PDFs have been submitted through doccollect, they become
available for annotation at brat in the doccollect directory.

Users need to login to brat to be allowed to create annotations.
The username and password are the ones specified when launching the docker container.

See [brat.md](brat.md) for more information.
