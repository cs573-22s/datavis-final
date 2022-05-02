### CS573 Final Project - Find Your TED 
### Team member: Yufei Lin & Mingjie Zeng
--------

Find Your TED is a visualization dashboard that can give you
suggestions about finding your favorite TED talks though the related networks between the videos. We hope this project can be useful and convenient to use by different users.

Project websites:  [websites link](https://jasminezzz9.github.io/CS573_Final_Project/)

Screen-cast: [screen-cast link](https://www.youtube.com/watch?v=WPHyvr4XTw8)

Process book: [process book link](https://github.com/YufeiLinUlysses/CS573_Final_Project/blob/main/Process%20book%20-%20Find%20Your%20TED.pdf)

Our final project source code is in the pages folder. The backend and frontend folders are our failed versions. The mongo folder contains the data processing.

## Goals
1. Show the ratio of the number of videos under different topics.
2. Show the relations between videos to let users find the next video to watch.

## Main Pages (usage)
1. Landing page:

Click on the button that says EXPLORE NOW to enter the function page.
<div align=center><img src="https://github.com/YufeiLinUlysses/CS573_Final_Project/blob/main/pics%20-%20readme/main-refine.jpg" width="50%" margin-left="20%"></div>

2. Topics page:

The top right corner is the search function for topic, fuzzy search available. The button in the lower right corner allows users to change the topics displayed.
<div align=center><img src="https://github.com/YufeiLinUlysses/CS573_Final_Project/blob/main/pics%20-%20readme/imp-topic.jpg" width="50%" margin-left="20%"></div>

3. Video list page:

Clicking the button inside the item will display the network page for the video and its related videos.
<div align=center><img src="https://github.com/YufeiLinUlysses/CS573_Final_Project/blob/main/pics%20-%20readme/imp-list.jpg" width="50%" margin-left="20%"></div>

4. Related videos page:

When you click the children nodes, the center node will change and its related videos will change too. Clicking the video link can direct users to the TED video page. The nodes can be dragged.
<div align=center><img src="https://github.com/YufeiLinUlysses/CS573_Final_Project/blob/main/pics%20-%20readme/imp-net.jpg" width="50%" margin-left="20%"></div>

   
## Achievement
1. Bubble chart and network graph
2. Interaction with bubble chart: When users hover over the bubble, the bubble will appear with a black border and a hover box to display the specific text content on the bubble. 
3. interaction with network graph: The user can click on a node to drag it around to change its position.
4. The search function for topics supports fuzzy search, users just need to type in some letters for a certain word.
5. Webpage developement: html + css + js + d3.

## Libraries and Reference
1. Official TED websites: https://www.ted.com/talks
2. [Using Social Network Graphs as Visualization Tools to Influence Peer Selection Decision-Making Strategies to Access Information About Complex Socioscientific Issues](https://www.tandfonline.com/doi/abs/10.1080/10508406.2011.563655)
3. [APPLICATION OF INTERACTIVE CHARTS IN THE EVALUATION OF SOCIO-ECONOMIC DEVELOPMENT OF REGIONS; THE CASE OF POLAND](http://acta.urk.edu.pl/APPLICATION-OF-INTERACTIVE-CHARTS-IN-THE-EVALUATION-OF-SOCIO-ECONOMIC-DEVELOPMENT,109093,0,2.html)
4. [How to Make Interactive Bubble Charts in D3.js](https://www.webtips.dev/how-to-make-interactive-bubble-charts-in-d3-js)
5. [networkD3 plots - GitHub Pages](https://christophergandrud.github.io/networkD3/)
