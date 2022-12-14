<html><p><img style="vertical-align: middle;" src="https://user-images.githubusercontent.com/30443495/196493267-c328669c-10af-4670-bbfa-e3029e7fb874.png" width="8%" align="left" /></p>
<h1>&nbsp; Loko - Client</h1><br></html>

**Loko Client** interacts with **loko-gateway** and **loko-orchestrator APIs**.

<b><ins>[Docs](https://loko-client.readthedocs.io/en/latest/)</ins></b> | 
<b><ins>[Tutorial](https://loko-client.readthedocs.io/en/latest/usage.html)</ins></b> | 
<b><ins>[LoKo AI](https://loko-ai.com/)</ins></b>

### Installation

```commandline
   (.venv) $ pip install loko-client
```

### FS Client example

FS Client interacts with **loko-orchestrator APIs**. You can use it to manage LoKo data.

```python
from loko_client.business.fs_client import FSClient

GATEWAY = 'http://localhost:9999/routes/'
fsclient = FSClient(gateway=GATEWAY)

### list directory content
print(fsclient.ls('data/data/datasets'))
### read file
content = fsclient.read('data/data/datasets/titanic.csv', mode='r')
print(content)
```

### Projects Client example

Projects Client interacts with **loko-orchestrator APIs** and you can use it to manage LoKo projects.

```python
from loko_client.business.projects_client import ProjectsClient

GATEWAY = 'http://localhost:9999/routes/'
pclient = ProjectsClient(gateway=GATEWAY)

### list projects
print(pclient.all_projects())
### list tasks
print(pclient.running_tasks())
```