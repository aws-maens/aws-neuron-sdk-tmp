Neuron Compiler FAQs
====================

Q: Where can I compile to Neuron?
---------------------------------

The one-time compilation step from the standard framework-level model to
Inferentia binary may be performed on any EC2 instance or even
on-premises.

We recommend using a high-performance compute server of choice (C5 or
z1d instance types), for the fastest compile times and ease of use with
a prebuilt `DLAMI <https://aws.amazon.com/machine-learning/amis/>`__.
Developers can also install Neuron in their own environments; this
approach may work well for example when building a large fleet for
inference, allowing the model creation, training and compilation to be
done in the training fleet, with the NEFF files being distributed by a
configuration management application to the inference fleet.

**Q: My current Neural Network is based on FP32, how can I use it with
Neuron?**

Inferentia chips support FP16, BFloat16 mixed-precision data-types and
INT8. It is common for Neural Networks to be trained in FP32, in which
case the trained graph needs to be converted to one of these data types
for execution on Inferentia. Neuron can compile and execute FP32 neural
nets by automatically converting them to BFloat16. Given an input using
FP32, the compiler output will ensure that the executed graph can accept
input inference requests in FP32. Also see :ref:`neuron-data-types`.

**Q: What are some of the important compiler defaults I should be aware
of?**

The compiler compiles the input graph for a single NeuronCore by
default. Using the The “\ ``num-neuroncores``\ ” option directs compiler
to direct compiled graph to run on a specified number of NeuronCores.
This number can be less than the total available NeuronCores on an
instance. See :ref:`appnote-performance-tuning` for more information
(TODO).

Q: Which operators does Neuron support?
---------------------------------------

see :ref:`neuron-supported-operators`.

If your model contains operators missing from the above list, please
post a message on the Neuron developer forum to let us know.

Q: Any operators that Neuron doesn't support?
---------------------------------------------

Models with control-flow and dynamic shapes are not supported. You will
need to partition the model using the framework prior to compilation.
See the :ref:`neuron-cc`.

Q: Will I need to recompile again if I updated runtime/driver version?
----------------------------------------------------------------------

The compiler and runtime are committed to maintaining compatibility for
major version releases with each other. The versoning is defined as
major.minor, with compatibility for all versions with the same major
number. If the versions mismatch, an error notification is logged and
the load will fail. This will then require the model to be recompiled.

**Q: I have a NEFF binary, how can I tell which compiler version
generated it?** We will bring a utility out to help with this soon.

Q: How long does it take to compile?
------------------------------------

It depends on the model and its size and complexity, but this generally
takes a few minutes.
