# brat

In the `brat` directory, run
```sh
docker build --build-arg username=<UserName> --build-arg password=<Password> --build-arg adminemail=<AdminEmail> -t <ImageName> .

docker run -dit --name <ContainerName> -p 8080:80 <ImageName>
```

Then in the browser, navigate to [localhost:8080/brat](http://localhost:8080/brat).  It may be that you have to refresh the first page if it only partially displays.

