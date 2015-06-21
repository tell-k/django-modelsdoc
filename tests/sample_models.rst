

.. contents::
   :local:


Poll(tests.models.Poll)
-----------------------------------------------------------------------------------------

::

  Poll

    * Poll has question and description fields
    

.. list-table::
   :header-rows: 1

   * - Fullname
     - Name
     - Type
     - PK
     - Unique
     - Index
     - Null/Blank
     - Comment
   * - ID
     - id
     - integer
     - True
     - True
     - 
     - Blank
     - 
   * - Question Name
     - question
     - varchar(255)
     - 
     - 
     - 
     - 
     - 
   * - Description
     - description
     - text
     - 
     - 
     - 
     - Blank
     - Description field allows Blank  
   * - Null Test
     - null_field
     - varchar(255)
     - 
     - 
     - 
     - Null
     - 
   * - Blank Test
     - blank_field
     - varchar(255)
     - 
     - 
     - 
     - Blank
     - 
   * - Both Test
     - both_field
     - varchar(255)
     - 
     - 
     - 
     - Both
     - 
   * - Index Test
     - index_field
     - varchar(255)
     - 
     - 
     - True
     - 
     -



Choice(tests.models.Choice)
-----------------------------------------------------------------------------------------

::

  Choice

    * Choice has poll reference
    * Choice has choices field
    

.. list-table::
   :header-rows: 1

   * - Fullname
     - Name
     - Type
     - PK
     - Unique
     - Index
     - Null/Blank
     - Comment
   * - ID
     - id
     - integer
     - True
     - True
     - 
     - Blank
     - 
   * - Poll
     - poll
     - integer
     - 
     - 
     - True
     - 
     - FK:tests.models.Poll
   * - Choice
     - choice
     - smallint
     - 
     - 
     - 
     - 
     - 1:test1, 2:test2, 3:test3



Vote(tests.models.Vote)
-----------------------------------------------------------------------------------------

::

  Vote

    * Vote has user reference
    * Vote has poll reference
    * Vote has choice reference
    

.. list-table::
   :header-rows: 1

   * - Fullname
     - Name
     - Type
     - PK
     - Unique
     - Index
     - Null/Blank
     - Comment
   * - ID
     - id
     - integer
     - True
     - True
     - 
     - Blank
     - 
   * - Voted User
     - user
     - integer
     - 
     - 
     - True
     - 
     - FK:django.contrib.auth.models.User
   * - Voted Poll
     - poll
     - integer
     - 
     - 
     - True
     - 
     - FK:tests.models.Poll
   * - Voted Choice
     - choice
     - integer
     - 
     - 
     - True
     - 
     - FK:tests.models.Choice


Options::

 unique_together : (('user', 'poll'),)


permission(django.contrib.auth.models.Permission)
-----------------------------------------------------------------------------------------

::

 
    The permissions system provides a way to assign permissions to specific
    users and groups of users.

    The permission system is used by the Django admin site, but may also be
    useful in your own code. The Django admin site uses permissions as follows:

        - The &quot;add&quot; permission limits the user&#39;s ability to view the &quot;add&quot; form
          and add an object.
        - The &quot;change&quot; permission limits a user&#39;s ability to view the change
          list, view the &quot;change&quot; form and change an object.
        - The &quot;delete&quot; permission limits the ability to delete an object.

    Permissions are set globally per type of object, not per specific object
    instance. It is possible to say &quot;Mary may change news stories,&quot; but it&#39;s
    not currently possible to say &quot;Mary may change news stories, but only the
    ones she created herself&quot; or &quot;Mary may only change news stories that have a
    certain status or publication date.&quot;

    Three basic permissions -- add, change and delete -- are automatically
    created for each Django model.
    

.. list-table::
   :header-rows: 1

   * - Fullname
     - Name
     - Type
     - PK
     - Unique
     - Index
     - Null/Blank
     - Comment
   * - ID
     - id
     - integer
     - True
     - True
     - 
     - Blank
     - 
   * - name
     - name
     - varchar(50)
     - 
     - 
     - 
     - 
     - 
   * - content type
     - content_type
     - integer
     - 
     - 
     - True
     - 
     - FK:django.contrib.contenttypes.models.ContentType
   * - codename
     - codename
     - varchar(100)
     - 
     - 
     - 
     - 
     -


Options::

 ordering : (u'content_type__app_label', u'content_type__model', u'codename')
 unique_together : ((u'content_type', u'codename'),)


group(django.contrib.auth.models.Group)
-----------------------------------------------------------------------------------------

::

 
    Groups are a generic way of categorizing users to apply permissions, or
    some other label, to those users. A user can belong to any number of
    groups.

    A user in a group automatically has all the permissions granted to that
    group. For example, if the group Site editors has the permission
    can_edit_home_page, any user in that group will have that permission.

    Beyond permissions, groups are a convenient way to categorize users to
    apply some label, or extended functionality, to them. For example, you
    could create a group &#39;Special users&#39;, and you could write code that would
    do special things to those users -- such as giving them access to a
    members-only portion of your site, or sending them members-only email
    messages.
    

.. list-table::
   :header-rows: 1

   * - Fullname
     - Name
     - Type
     - PK
     - Unique
     - Index
     - Null/Blank
     - Comment
   * - ID
     - id
     - integer
     - True
     - True
     - 
     - Blank
     - 
   * - name
     - name
     - varchar(80)
     - 
     - True
     - 
     - 
     -



user(django.contrib.auth.models.User)
-----------------------------------------------------------------------------------------

::

 
    Users within the Django authentication system are represented by this
    model.

    Username, password and email are required. Other fields are optional.
    

.. list-table::
   :header-rows: 1

   * - Fullname
     - Name
     - Type
     - PK
     - Unique
     - Index
     - Null/Blank
     - Comment
   * - ID
     - id
     - integer
     - True
     - True
     - 
     - Blank
     - 
   * - password
     - password
     - varchar(128)
     - 
     - 
     - 
     - 
     - 
   * - last login
     - last_login
     - datetime
     - 
     - 
     - 
     - 
     - 
   * - superuser status
     - is_superuser
     - bool
     - 
     - 
     - 
     - Blank
     - 
   * - username
     - username
     - varchar(30)
     - 
     - True
     - 
     - 
     - 
   * - first name
     - first_name
     - varchar(30)
     - 
     - 
     - 
     - Blank
     - 
   * - last name
     - last_name
     - varchar(30)
     - 
     - 
     - 
     - Blank
     - 
   * - email address
     - email
     - varchar(75)
     - 
     - 
     - 
     - Blank
     - 
   * - staff status
     - is_staff
     - bool
     - 
     - 
     - 
     - Blank
     - 
   * - active
     - is_active
     - bool
     - 
     - 
     - 
     - Blank
     - 
   * - date joined
     - date_joined
     - datetime
     - 
     - 
     - 
     - 
     -


Options::

 swappable : AUTH_USER_MODEL


content type(django.contrib.contenttypes.models.ContentType)
-----------------------------------------------------------------------------------------

::

 ContentType(id, name, app_label, model)

.. list-table::
   :header-rows: 1

   * - Fullname
     - Name
     - Type
     - PK
     - Unique
     - Index
     - Null/Blank
     - Comment
   * - ID
     - id
     - integer
     - True
     - True
     - 
     - Blank
     - 
   * - name
     - name
     - varchar(100)
     - 
     - 
     - 
     - 
     - 
   * - app label
     - app_label
     - varchar(100)
     - 
     - 
     - 
     - 
     - 
   * - python model class name
     - model
     - varchar(100)
     - 
     - 
     - 
     - 
     -


Options::

 ordering : ('name',)
 unique_together : (('app_label', 'model'),)


