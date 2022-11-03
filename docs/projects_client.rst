Projects Client
================

Projects Client interacts with **loko-orchestrator APIs** and you can use it to manage LoKo projects.
We provide both a synchronous and asynchronous client.

To use Projects Client you have to provide the gateway url. Usually, when you're working on a docker container deployed
on the loko network the url is ``http://gateway:8080/routes/``. Otherwise, the url is
``http://localhost:9999/routes/``.

.. code-block:: python

    gw = 'http://gateway:8080/routes/'
    pclient = ProjectsClient(gateway=gw)

If you need the **async** version:

.. code-block:: python

    gw = 'http://gateway:8080/routes/'
    pclient = AsyncProjectsClient(gateway=gw)


Projects Management
-------------------

You can list all LoKo **projects** using:

.. code-block:: python

    pclient.all_projects()

You can check the project's **deployment status** and **deploy**/**undeploy** a project using:

.. code-block:: python

    prj_id = 'first_project'
    pclient.undeploy(prj_id)
    print(pclient.deployment_status(prj_id))
    pclient.deploy(prj_id)
    print(pclient.deployment_status(prj_id))

To get information of a specific **project** use:

.. code-block:: python

    prj = pclient.get_project(prj_id)


The result is a :py:meth:`~loko_client.model.projects.Project` object. We'll see how to get projects details in the
next section.

Project Details
---------------

You can get all project's **tabs** using:

.. code-block:: python

    prj.tabs.all()

Attribute `tabs` contains all :py:meth:`~loko_client.model.projects.Nodes` and
:py:meth:`~loko_client.model.projects.Edges` of a tab, in this case named `main`:

.. code-block:: python

    nodes = prj.tabs.main.nodes.nodes
    edges = prj.tabs.main.edges.edges

You can also use square brackets to access tabs:

.. code-block:: python

    all_nodes = []
    for tab in prj.tabs.all():
        all_nodes += prj.tabs[tab].nodes.nodes.values()

You can **search** for specific nodes using:

.. code-block:: python

    res = prj.tabs.main.nodes.search('data.name', 'HTTP Request')

    for node_id in res:
        node = prj.tabs.main.nodes[node_id]
        print(node.data['name'])

In this example we want to find all `HTTP Request` nodes in `first_project` project, in tab `main`. To search for
nested keys use the dot notation. If you want to search nodes using the alias, you can use:

.. code-block:: python

    res = prj.tabs.main.nodes.search('data.options.values.alias', 'My block')

    for node_id in res:
        node = prj.tabs.main.nodes[node_id]
        print(node.data['options']['values']['alias'])

Tasks Management
----------------

To get running **tasks**, use:

.. code-block:: python

    running = pclient.running_tasks()

    for task in running:

        print(f'project: {task["project"]} - tab: {task["graph"]} - node_name: {task["source"]} - '
              f'uid: {task["uid"]} - user: {task["user"]} - started: {task["startedAt"]}')

You can **cancel** a task using its uid:

.. code-block:: python

    uid = 'f324b286-3df5-4966-923d-c9af5c94690e'
    pclient.cancel_task(uid=uid)

You can **start** tasks using the `project_id` and `component_id`:

.. code-block:: python

    component_id = list(pclient.get_project('first_project').tabs.main.nodes.search('data.options.values.alias',
                                                                                    'My block'))[0]
    pclient.trigger('first_project', component_id)
    print(pclient.running_tasks())

We first have to find the *component_id* we are interested in. In this case we search for the component named
'My block'. Then we can trigger the component and check the running tasks.