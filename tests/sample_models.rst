


.. contents::
   :local:


permission(django.contrib.auth.models.Permission)
-----------------------------------------------------------------------------------------

::

 
    The permissions system provides a way to assign permissions to specific
    users and groups of users.

    The permission system is used by the Django admin site, but may also be
    useful in your own code. The Django admin site uses permissions as follows:

        - The "add" permission limits the user's ability to view the "add" form
          and add an object.
        - The "change" permission limits a user's ability to view the change
          list, view the "change" form and change an object.
        - The "delete" permission limits the ability to delete an object.

    Permissions are set globally per type of object, not per specific object
    instance. It is possible to say "Mary may change news stories," but it's
    not currently possible to say "Mary may change news stories, but only the
    ones she created herself" or "Mary may only change news stories that have a
    certain status or publication date."

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
     - varchar(255)
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
 default_permissions : (u'add', u'change', u'delete')


group-permission relationship(django.contrib.auth.models.Group_permissions)
-----------------------------------------------------------------------------------------

::

 Group_permissions(id, group, permission)

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
   * - group
     - group
     - integer
     - 
     - 
     - True
     - 
     - FK:django.contrib.auth.models.Group
   * - permission
     - permission
     - integer
     - 
     - 
     - True
     - 
     - FK:django.contrib.auth.models.Permission


Options::

 unique_together : (('group', 'permission'),)
 default_permissions : (u'add', u'change', u'delete')


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
    could create a group 'Special users', and you could write code that would
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
   * - permissions
     - permissions
     - 
     - 
     - 
     - 
     - Blank
     - M2M:django.contrib.auth.models.Permission (through: django.contrib.auth.models.Group_permissions)


Options::

 default_permissions : (u'add', u'change', u'delete')


user-group relationship(django.contrib.auth.models.User_groups)
-----------------------------------------------------------------------------------------

::

 User_groups(id, user, group)

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
   * - user
     - user
     - integer
     - 
     - 
     - True
     - 
     - FK:django.contrib.auth.models.User
   * - group
     - group
     - integer
     - 
     - 
     - True
     - 
     - FK:django.contrib.auth.models.Group


Options::

 unique_together : (('user', 'group'),)
 default_permissions : (u'add', u'change', u'delete')


user-permission relationship(django.contrib.auth.models.User_user_permissions)
-----------------------------------------------------------------------------------------

::

 User_user_permissions(id, user, permission)

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
   * - user
     - user
     - integer
     - 
     - 
     - True
     - 
     - FK:django.contrib.auth.models.User
   * - permission
     - permission
     - integer
     - 
     - 
     - True
     - 
     - FK:django.contrib.auth.models.Permission


Options::

 unique_together : (('user', 'permission'),)
 default_permissions : (u'add', u'change', u'delete')


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
     - Both
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
     - varchar(254)
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
   * - groups
     - groups
     - 
     - 
     - 
     - 
     - Blank
     - M2M:django.contrib.auth.models.Group (through: django.contrib.auth.models.User_groups)
   * - user permissions
     - user_permissions
     - 
     - 
     - 
     - 
     - Blank
     - M2M:django.contrib.auth.models.Permission (through: django.contrib.auth.models.User_user_permissions)


Options::

 default_permissions : (u'add', u'change', u'delete')
 swappable : AUTH_USER_MODEL


content type(django.contrib.contenttypes.models.ContentType)
-----------------------------------------------------------------------------------------

::

 ContentType(id, app_label, model)

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

 unique_together : ((u'app_label', u'model'),)
 default_permissions : (u'add', u'change', u'delete')


site(django.contrib.sites.models.Site)
-----------------------------------------------------------------------------------------

::

 Site(id, domain, name)

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
   * - domain name
     - domain
     - varchar(100)
     - 
     - 
     - 
     - 
     - 
   * - display name
     - name
     - varchar(50)
     - 
     - 
     - 
     - 
     -


Options::

 ordering : (u'domain',)
 default_permissions : (u'add', u'change', u'delete')


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


Options::

 default_permissions : (u'add', u'change', u'delete')


Genre(tests.models.Genre)
-----------------------------------------------------------------------------------------

::

  Genre

    * Choice has genre
    

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
   * - Genre name
     - name
     - varchar(255)
     - 
     - 
     - 
     - 
     -


Options::

 default_permissions : (u'add', u'change', u'delete')


choice-genre relationship(tests.models.Choice_genres)
-----------------------------------------------------------------------------------------

::

 Choice_genres(id, choice, genre)

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
   * - choice
     - choice
     - integer
     - 
     - 
     - True
     - 
     - FK:tests.models.Choice
   * - genre
     - genre
     - integer
     - 
     - 
     - True
     - 
     - FK:tests.models.Genre


Options::

 unique_together : (('choice', 'genre'),)
 default_permissions : (u'add', u'change', u'delete')


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
   * - Genre
     - genres
     - 
     - 
     - 
     - 
     - 
     - M2M:tests.models.Genre (through: tests.models.Choice_genres)


Options::

 default_permissions : (u'add', u'change', u'delete')


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
 default_permissions : (u'add', u'change', u'delete')



