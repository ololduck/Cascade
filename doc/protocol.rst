Protocol
========

We have to be able to:

 * recieve current torrents.
 * send torrent files
 * pause/resume/delete torrents (?)


+-----------+-----------------------------+
| Syntax    | description                 |
+===========+=============================+
| PUT file  | sends torrent file          |
+-----------+-----------------------------+



PUT
~~~

sent::

   PUT "/path/to/file.torrent" size_in_bit

resp::

   200 OK Proceed to file upload

sent::

   <FULL FILE>

resp::

   200 OK File uploaded
