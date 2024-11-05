We are implementing a delivery system named as GatorGlide
Delivery Co which is a tech sabvy beacon of efficient t logistics
inspired by the swift movements of the alligator. It is planning to
elevate its software infrastructure to meet the growing demands of
customers. The new system aims to optimize order management,
delivery routes, and enhance overall efficiency. They use AVL trees to
intricately store the order priorities and ETAs to manage the orders
efficiently.
Class Descriptions:
Node: Represents a node in the AVL tree, holding key-value pairs
along with pointers to left and right child nodes and the height of the
node for balancing purposes.
key: A numerical value representing the priority or ETA (Estimated
Time of Arrival) of an order. It serves as the sorting criterion within
the AVL Tree.
val: An Order object containing all the information about a delivery
order.
left: A reference to the left child node in the AVL Tree.
right: A reference to the right child node in the AVL Tree.
height: An integer representing the height of the node within the
AVL Tree, used to maintain balance during insertions and deletions.
Order: Represents an order with attributes like order ID, current
system time, order value, delivery time, priority (calculated based on
order value and current system time), and ETA.
Class Order
order_id: A unique identifier for the order.
current_system_time: The current time in the system when the
order is being processed or created.
order_value: The monetary value of the order.
delivery_time: The time required to deliver the order.
priority: A calculated value representing the order's priority, which
combines the order value and current system time using a weighted
formula. Higher priorities indicate orders that should be processed
sooner.
eta: The estimated time of arrival (delivery) for the order. This is
calculated based on the order's priority, current system time, and
delivery time.
AVLTree: A class implementing the AVL tree data structure that
supports insertion, deletion, and rotations to maintain a balanced
tree. It also includes utility methods to get a node's height, balance
factor, and in-order traversal.
This class itself does not have attributes that are directly instantiated
but operates on Node instances to manage the AVL tree structure. It
includes methods for:
 Inserting a new node based on key comparison.
 Deleting a node while maintaining the AVL tree's balance.
 Rotating nodes left or right to keep the tree balanced.
 Getting the height of a node within the tree.
 Computing the balance factor of a node
GatorDelivery: The main class that encapsulates the order
management system. It uses two AVL trees to manage orders based
on priority and ETA. It supports creating, cancelling, updating
delivery time of orders, retrieving the rank of an order, printing
specific orders, and printing orders within a given time frame.
Functions
Creating an Order (createOrder):
 An order is created with given attributes.
 The order's priority is calculated, and the order is inserted into
the priority tree.
 If it's the only order, its ETA is set, and delivery begins.
 If there are other orders, it updates the ETAs of subsequent
orders and records any changes.
Cancelling an Order (cancelOrder):
 Searches for the order in the trees.
 If found, the order is removed from both trees.
 ETAs of subsequent orders are updated accordingly.
Updating Delivery Time (updat
Updating Delivery Time (updateTime):
 Finds the specified order.
 Updates the delivery time.
 Adjusts ETAs for this order and potentially for subsequent
orders.
Getting Rank of an Order (getRankOfOrder):
 Determines the order's position within the priority tree,
indicating how many orders are ahead of it.
Printing an Order (printOrder):
 Searches for an order by ID and prints its details.
Printing Orders Within a Time Frame (printTime):
 Finds and prints orders that are scheduled for delivery within
the specified time range.
Quitting (quit):
 Simulates the delivery of remaining orders and cleans up the
system.
Logic And Structure:
The main logic of the program is to create an avl tree put it in a list
such that the order that is being delivered is appended into the last
of the list so that operations such as update and cancel can be done
with low complexity without running multiple if else statement in
this way we create a list search the index of the specified order and o
the needful operations
System Flow:
The system begins by initializing an instance of GatorDelivery, which
manages orders through AVL trees based on priorities (determined
by order value and time) and ETAs. Orders can be added, cancelled,
or updated in real-time, with the system adjusting ETAs and order
sequences as needed.
The AVL tree structure ensures that operations like insertion,
deletion, and balance maintenance are performed efficiently, with a
time complexity of O(log n) for most operations, making it suitable
for real-time order management in a delivery system.
Reporting and Logging:
The system supports logging and reporting through writing to a
specified output file. This includes creating, updating, cancelling
orders, and printing specific orders or orders within a time frame.
The log captures significant events and changes in the order queue,
providing a detailed record of the system's operation over time.
In summary, the code implements a sophisticated order
management system that dynamically adjusts to changes in order
priority and delivery timings, ensuring efficient processing and
management of delivery orders.
