## Client使用

* 点击可执行文件或在目录下输入`python3 main.py`即可运行client

- 首先使用Client一定要先进行连接，填入IP、端口、用户名及密码信息后，点击connect按钮即可完成连接
- 连接完成后，可以看到主程序分为两大主要窗口，上半部分显示当前目录的文件信息，在其中可以进行目录跳转、上传下载、新建、修改、剪切、删除目录等操作。其中目录跳转通过双击任意文件夹即可实现进入文件夹，通过点击子文件夹的".."目录即可回到父目录，而其他操作均通过在相应文件夹或文件上右键完成。下半部分窗口则是文件传输列表，显示目前未完成的文件传输内容。当有文件传输发生时，上半部分会被锁定，不允许用户再进行相关的操作。用户通过右键传输项可以实现对传输项的控制，包括暂停、继续以及取消。
- PORT和PASV模式的切换放置于菜单栏的Option菜单中，点击PORT或PASV可以选择相应的模式。当选择PORT模式后，程序的HOST和PORT输入框会允许输入，用户完成输入后点击PORT按钮即可完成PORT连接，点击PASV则可再次切换回PASV模式。