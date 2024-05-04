======================
YGOPRODECK API Wrapper
======================

------------
Installation
------------

You can install it with pip3:

.. code-block:: bash

    pip3 install --upgrade git+https://github.com/EllieJaybee/yugioh.git

-----
Usage
-----

.. code-block:: python

    import yugioh
    
    card = yugioh.get_card("The Wicked Dreadroot") #Accepts both name and ID
    print(card.name) #Returns "The Wicked Dreadroot"
    print(card.archetype) #Returns "Wicked God"
    print(card.atk) #Returns "4000"

------------------
Monster Attributes
------------------

+--------------------+---------------------------------+
| Attribute          | Description                     |
+--------------------+---------------------------------+
| name               | The card's name                 |
+--------------------+---------------------------------+
| archetype          | The card's archetype            |
+--------------------+---------------------------------+
| atk                | The card's attack points        |
+--------------------+---------------------------------+
| attribute          | The card's attribute            |
+--------------------+---------------------------------+
| def\_              | The card's defense points       |
+--------------------+---------------------------------+
| desc               | The card's description          |
+--------------------+---------------------------------+
| id                 | The card's ID                   |
+--------------------+---------------------------------+
| level              | The card's level                |
+--------------------+---------------------------------+
| race               | The card's "race" (type)        |
+--------------------+---------------------------------+
| type               | Monster/Normal card             |
+--------------------+---------------------------------+

---------------------------
Spell/Trap/Skill Attributes
---------------------------

+--------------------+---------------------------------+
| Attribute          | Description                     |
+--------------------+---------------------------------+
| desc               | The card's description          |
+--------------------+---------------------------------+
| id                 | The card's ID                   |
+--------------------+---------------------------------+
| name               | The card's name                 |
+--------------------+---------------------------------+
| type               | The card's type                 |
+--------------------+---------------------------------+
| race               | The card's "race"               |
+--------------------+---------------------------------+

You can get further documentation from `here <https://ygoprodeck.com/api-guide/>`_.

Please report all issues `here <https://github.com/EllieJaybee/yugioh/issues>`_.
