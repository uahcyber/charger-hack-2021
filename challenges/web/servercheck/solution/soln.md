solution
========

this is a command injection challenge.

since the output on the website is the output of the `ping` command, it can be assumed that whatever is typed into the text box will be processed on the command line. 

to exploit this, we can submit something like:
```bash 
127.0.0.1 && ls
```

this will yield both the output of the ping command as well as a directory listing of the web server's working directory. from here, we can see that there is a flag.txt file.

the final payload to get the flag would be:

```bash
127.0.0.1 && cat flag.txt
```