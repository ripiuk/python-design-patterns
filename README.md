# Design Patterns in Python

* Creational
    * [Simple Factory](creational/01_simple_factory) - is an object for creating other objects.
    * [Factory Method](creational/02_factory_method) -  uses inheritance and relies on a subclass to handle the desired object instantiation.
    * [Abstract Factory](creational/03_abstract_factory) - class delegates the responsibility of object instantiation to another object via composition.
    * [Builder](creational/04_builder) - separate the construction of a complex object from its representation.
    * [Prototype](creational/05_prototype) - helps us with creating object clones.
    * [Singleton](creational/06_singleton) - involves a single class which is responsible to create an object while making sure that only single object gets created.
    * [Borg](creational/07_borg) - singleton behavior, but instead of having only one instance
of a class, there are multiple instances that share the same state.
* Structural
    * [Adapter](structural/01_adapter) - helps us make two incompatible interfaces compatible.
    * [Bridge](structural/02_bridge) - involves an interface which acts as a bridge which makes the functionality of concrete classes independent from interface implementer classes.