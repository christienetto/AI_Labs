# Project Progress and Details

## 1. Which programming language are you using?
I am using **Python** as the main programming language for my project since I am more familiar with it compared to others. I might be testing the application on the web using **Flask**. Additionally, I will use **OpenSSL** for displaying the map.

## 2. Also, mention any other languages you are proficient in to the extent that you could peer-review projects written in them.
I am proficient in **Go (Golang)**, **JavaScript** (with **Svelte** and **Next.js**), and **SQL** (with tools like **SQLC**). I would feel confident reviewing projects written in these languages.

## 3. What algorithms and data structures will you implement in your project?
In my project, I will likely use algorithms for data querying and possibly pathfinding algorithms if dealing with transit routes (e.g., **Dijkstra’s algorithm** for finding the shortest path). **Graphs** will be the primary data structure used to represent the transit routes and connections.

## 4. What problem are you solving?
The goal of the project is to create an app that queries data from **Digitransit** and displays it with an emphasis on processing and visualizing this data. The problem to be solved is improving access to real-time transit information and potentially offering insights based on the data provided by **HSL**.

## 5. What inputs does the program receive, and how are they used?
The program will receive input in the form of transit-related data, such as **bus routes**, **station locations**, and **schedules** from the **Digitransit API**. This data will be used to display real-time information, calculate the shortest routes, or analyze transit patterns.

## 6. Expected time and space complexities (e.g., Big-O analysis)
- **Time complexity**: Since the project involves querying data from an API and potentially implementing graph-based algorithms (e.g., for shortest path), the time complexity of these queries could be around **O(n log n)** for sorting or **O(V + E)** for graph algorithms where **V** is the number of vertices (stations) and **E** is the number of edges (connections between stations). 
- **Space complexity**: The space complexity will primarily depend on the size of the graph and the number of data points retrieved from the API. Storing this data will take **O(V + E)** space in memory for the graph structure.

## 7. Find out as much as possible. You are not expected to prove or measure anything yourself.
I will look into the **Digitransit API** documentation to fully understand the types of data available and their structure. Understanding this will help optimize both time and space complexity when querying and processing the data.

## 8. Use time and space complexity as a tool to understand how to approach the project.
By considering the time and space complexities, I will know how to efficiently handle the data, especially as it scales. This will guide decisions like data structures (e.g., using adjacency lists for graph representations) and help prioritize algorithm efficiency.

## 9. Check Wikipedia or other reliable sources, and ensure you understand where these complexities come from in your algorithm. Why does your algorithm require that amount of time?
I will refer to reliable sources like Wikipedia or algorithm textbooks to get a clear understanding of the complexities. For example, **Dijkstra's algorithm** runs in **O((V + E) log V)** time using a priority queue because it processes each vertex and edge in the graph to find the shortest path. The time complexity arises from the need to visit each node and edge and update distances.

## 10. References
- Digitransit API documentation
- Wikipedia pages on **Dijkstra’s algorithm** and **graph theory**
- Python documentation on **Flask** and **OpenSSL**


Core of the Project is that it is a path finding algorithm and uses HSL data to show the shortest path
