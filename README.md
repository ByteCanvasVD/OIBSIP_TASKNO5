# OIBSIP_TASKNO5
Assistance regarding an internship project at Oasis Infrobyte
<h3>5.Chat Aplication</h3>
<b>Project Overview:<br></b>
<p>Project Overview: Using Tkinter on the client side, this project is a powerful chat program featuring a graphical user interface (GUI). It involves several clients with real-time communication capabilities and a server. User identification, support for numerous chat rooms.
</p>
<p>Specifics of Implementation:<br>
1. The Chat Application Server<br> located at Chat_Application_server.py:
Message broadcasting to all connected clients and user connection management fall under the purview of the server.
Socket programming is used to provide real-time communication.
User data (username, socket) is stored in a dictionary called users.
The server is ready for incoming connections at port 12346.
It connects, gets the username from the client, and opens a new thread for the client's communication.
As soon as a message is received, it is sent to every client.<br>
2. Chat Application Client:<br>
 Clients provide a Tkinter GUI with a chat box, message entry, and send button (Chat Application Client.py and Chat Application Client2.py).
Socket programming allows clients to establish connections with servers.
Clients send the server their usernames when they join.
A another thread keeps an eye out for new messages and modifies the chat area accordingly.
By typing text and selecting the "Send" button, clients can send messages to the server.
</p>
<h3>The project's flow: </h3>
<p>1)Server configuration<br>
The server is up and running, listening on port 12346 for incoming connections.<br>
2)Initialization of the client:<br>
Clients connect to the server, set up a Tkinter GUI, and give their usernames.<br>
3)Interaction:<br>
By entering text into the entry area and selecting the "Send" button, customers can send messages.
Messages from clients are received by the server, which then distributes them to all clients that are linked.<br>
4)User Communication:<br>
The server sends messages to the clients, who then update their chat boxes.</p>
<h3>format of output:</h3>
<p>1.Output from Server:<br>
The server prints notifications about user connections and listening on a particular port.<br>
2.Client Graphical User Interface:<br>
The chat window, message entry, and send button are all part of the client GUI.
The chat box shows the user's sent messages as well as any incoming messages from other users.
</p>
<h3>Important to remember Note: </h3>
 <p>Chat_Application_client.py and Chat_Application_client2.py, the client codes that were provided, are be the same. Please ensure that any changes you planned to make are made.</p>
