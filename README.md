# MJPEG-Relay
Docker image containing a relay that allows simultaneous connections to multiple MJPEG streams


# What is this for?
In my case, I wanted to include my cameras' video streams into my smarthome system. The only stream my cameras were offering, was MJPEG - the issue: only one single user can access a stream simultaneously. So I built a tool that solves this issue by caching the feed and providing streams that can be accessed by multiple users in parallel.

# What to take care of?
The stream is not encrypted - since I simply did not needed. If there is any interest, it should be pretty easy to implement it.
