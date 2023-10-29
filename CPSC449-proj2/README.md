# Project 2

## Usage

First, create the databases with the following command:

```bash
./bin/init.sh
```

Then, run the server with the following command:

```bash
foreman start --formation enrollment=3,user_primary=1,user_secondary-1=1,user_secondary-2=1user_krakend=1,enroll_krakend=1 
```
