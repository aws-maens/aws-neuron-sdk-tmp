.. _neuron-gettingstarted:

Getting started
===============

Neuron SDK's documentation provide the information needed to enable you
start developing and deploying your ML inference application, depending
if you are a first time user or if you are looking for specific topic documentation, this section provide you with the
information you need to quickly navigate your way into using Neuron for your ML applications.

First time user
---------------

If you are a first-time-user, the following steps are
recommended for you to get started with Neuron:

#. Run your first Neuron ML application by following the instructions in
   one of the following Getting Started tutorials to get familiar with
   Neuron development flow of your ML framework of choice:

   -  :ref:`tensorflow-resnet50`
   -  :ref:`pytorch-restent50`
   -  :ref:`mxnet-resnet50`

#. Get familiar with Neuron fundamentals and tools:

   -  Learn :ref:`neuron-fundamentals` : such as
      :ref:`neuron-data-types`, :ref:`neuron-batching` and
      :ref:`neuroncore-pipeline`, learning Neuron fundamentals will help
      you utilize Neuron to develop a highly optimized ML application.
   -  Get familiar with :ref:`neuron-cc`,\ :ref:`neuron-runtime` and
      :ref:`neuron-tools` by going over the overview sections and
      briefly reading about the supported features and capabilities of
      Neuron Compiler, Runtime and Tools.

#. Deploy Neuron ML application at scale by learning how to tune,
   optimize and deploy your ML application at scale by following the
   instructions of one of the HowTo guides at
   :ref:`deploy-ml-application`.


Navigate documentation
----------------------

Tutorials
~~~~~~~~~

Explore more Tutorials and examples at:

-  :ref:`tensorflow-tutorials`
-  :ref:`pytorch-tutorials`
-  :ref:`mxnet-tutorials`
-  :ref:`mxnet-tutorials`
-  :ref:`Neuron Containers Tutorials and Examples <containers-tutorials>`

ML Frameworks
~~~~~~~~~~~~~

You can find Neuron supported ML Frameworks at:

-  :ref:`neuron-tensorflow`
-  :ref:`neuron-pytorch`
-  :ref:`neuron-mxnet`

ML Inference Models
~~~~~~~~~~~~~~~~~~~

You can find ML Inference models tutorials at:

-  Computer Vision

   -  :ref:`Tensor Flow <tensorflow-computervision>`
   -  :ref:`PyTorch <pytorch-computervision>`
   -  :ref:`MXNet <mxnet-computervision>`

-  Natural Language Processing

   -  :ref:`Tensor Flow <tensorflow-nlp>`
   -  :ref:`PyTorch <pytorch-nlp>`
   -  :ref:`MXNet <mxnet-nlp>`

Performance optimization
~~~~~~~~~~~~~~~~~~~~~~~~

The following steps are recommended for you to achieve highly optimized
neuron application:

#. Get familiar with Neuron fundamentals and tools (If you are not):

   -  Learn :ref:`neuron-fundamentals` : such as
      :ref:`neuron-data-types`, :ref:`neuron-batching` and
      :ref:`neuroncore-pipeline`, learning Neuron fundenetals will help
      you utilize Neuron to develop a highly optimized ML application.
   -  Get familiar with :ref:`neuron-cc`,\ :ref:`neuron-runtime` and
      :ref:`neuron-tools` by going over the overview sections and
      briefly reading about the supported features and capabilities of
      Neuron Compiler, Runtime and Tools.

#. Learn how to optimize your application by going over the HowTo guides
   at :ref:`performance-optimization` .

Containers Support
~~~~~~~~~~~~~~~~~~

visit :ref:`neuron-containers` for more information about Neuron
containers support and more :ref:`containers-tutorials`.


.. _install-neuron:

Installing Neuron
-----------------

To use Neuron you can use a pre-built Amazon Machine Images (DLAMI) or
DL containers or install Neuron software on your own instances. To
ensure you have the latest Neuron version we recommend to either install
it on your own instance, or to check for the installed version when
using DLAMI or DL containers.

You can :ref:`neuron-install-guide` if you already have an environment
you'd like to continue using.


.. toctree::
   :maxdepth: 1

   neuron-install-guide
   dlami
   dlcontainers