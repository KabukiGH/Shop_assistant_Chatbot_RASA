# Shop_assistant_Chatbot_RASA
Software designed for Pepper robot using ROS
Project develops a robotic assistant for helping people in managing their personal shopping list. To communicate with the user, the robotic platform must use a microphone. 
	The robot must manage a different list for each person it discusses with:
  
- If a new person is met, the robot asks his/her name and creates a new shopping list
- If it’s not a new user, the robot should recognize him/her from either face or voice
	Once the identity of the user is recognized, the robot must allow the user to:
- Add a new item to the shopping list
- Remove an item from the shopping list
- Show the shopping list
- Empty the shopping list
The shopping list are filled with elements that are identified by a name and a quantity. 

It's also have environmental constraints, such as the distance between the user and the robot (should be less than 2 meters), no ambient noises during the conversation and only 1 user can talk to the robot at a time.
	For the code of this project, I will be using Python, with the ROS package. The robot we will be using to try our software will be the robot Pepper.

![image](https://user-images.githubusercontent.com/99291705/156606167-1b565459-a0ee-4ca6-a0d8-83678c36e986.png)

Picture 1: Architecture of the code

Detailed Architecture

For this project it's using ROS (Robot Operating System). It is a set of software libraries and tools that helps build robot applications. The applications are designed as unit known as Nodes. In a robot system, sensors, motion controllers or algorithms components can be nodes. Nodes communicate with each other via Topic, Service Invocation or Actions. This communication has publish/subscribe architecture where data produced and published by a node is subscribed by another. The data types used in topic communication are called message.
	The ROS Master provides naming and registration services to the rest of the nodes in the system. His role is to enable individual nodes to locate one another. Once they have located each other, they can communicate.

Implement Design Choice

For this project, we decided to use RASA. It is an open-source AI for buildings conversational chatbots. It is used to automate the text and voice-based assistants.
RASA has advantages such as:
- Being open-source
- Being flexible: you can add/remove what you want so it fits better to your project
- Learning on its own
RASA works on 3 main elements that are Natural Language Understanding (NLU), Natural Language Generation (NLG) and Dialogue Management. NLU converts text into vectors to identify the intention of the sentence. It is tagging each work with a part of speech (noun, verb, ect) and then regroup them into groups. It first finds the request in the sentence and then extract the entity.
NLG is taking inputs of non-linguistic format and converts it into a human-understandable form.
The Dialogue Management is – as its name suggest – managing the dialogue with the user.

