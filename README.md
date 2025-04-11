Performance Test (Load Test) for Music Web App (Youbloom and youbloomconnect)

Overview

This performance test aims to evaluate the load capacity and response times of a music-based web application that allows users to create shows, follow artists, and interact as fans. The test will simulate real-world traffic using Locust, a Python-based load-testing tool.

Objectives

Assess the scalability and stability of the application.

Measure response times for critical user interactions.

Identify bottlenecks and potential failure points under high load.

Ensure optimal user experience under peak traffic conditions.

Test Scenarios

User Signup & Login

New users register with the platform.

Existing users log in.

Show Creation

Authenticated users (artists) create new shows.

Users upload media files (images, posters, etc.).

Check response times for show listings.

Fan Engagement

Fans follow artists.

Fans like and comment on shows.

Fans share show details.

Artist Profile Management

Artists update their profiles.

Artists add or remove events.

Load Handling

Simulate a high number of concurrent users.

Measure response times and system resource utilization.

Test Tools & Environment

Testing Tool: Locust

Programming Language: Python

Environment:

Staging environment matching production.

Database with realistic test data.

Performance Metrics

Response Time: Measure time taken for each request.

Throughput: Number of requests handled per second.

Error Rate: Percentage of failed requests.

CPU & Memory Usage: System resource consumption.

Test Execution

Install dependencies:

pip install locust faker requests

Run the Locust test:

locust -f load_test.py --host=https://www.Youbloom.com & https://www.youbloomconnect

Monitor test execution via Locust’s web UI (http://localhost:8089).

Expected Outcomes

The system should handle at least 500 concurrent users without degradation.

Average response time should remain under 2 seconds.

No critical failures under peak load.

Identify areas requiring optimization (e.g., database queries, caching).

Reporting & Analysis

Find attached reports based on the Two hosts in the results folder.
