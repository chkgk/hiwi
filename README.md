# Hiwi

Hiwi is a companion tool for otree that makes it easy to share experiments you created.

## Features
- package exeriments in a single zip file
- publish packages on a repository
- integrate experiments in otree installations right from the repository


## Quickstart
Integrate an experiment from the repository:
```
hiwi integrate <experiment_name>
```

Integrate an experiment from a zip file created by hiwi:
```
hiwi integrate --local <experiment_name>
```

Package an experiment:
```
hiwi package <name_in_session_config>
```

Package and publish an experiment on the repo:
``` 
hiwi publish <name_in_session_config>
```