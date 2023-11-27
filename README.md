# demo-argpase-pipeline

This repo is a sample pipeline using `argparse` to parse command line arguments. The pipeline has a base config that your can find at `./config.yaml`. The pipeline can run
with the default config using the following command. 

```bash 
poetry install
poetry run python3 main.py
```

The pipeline config can be overwritten at run time using the following command. 

```bash
python main.py --env dev --author setsuna
```

The heirachary of config is as follows.

`base config -> env config -> command line args`

The pipeline will use the command line args to overwrite the env config, and the env config will overwrite the base config.

A great a pattern for any pipeline pipeline that will work for multiple environments.

## References

- https://docs.python.org/3/library/argparse.html