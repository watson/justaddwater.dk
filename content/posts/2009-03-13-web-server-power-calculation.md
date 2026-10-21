---
title: "Web Server Power Calculation"
date: "2009-03-13T10:45:05"
slug: "web-server-power-calculation"
url: "/2009/03/13/web-server-power-calculation/"
wp_id: 1053
categories: ["Web Development", "Website"]
tags: ["power consumption", "web server", "work"]
---

In our company's basement a small server room where we put a few sandbox machines we use for quickly starting up projects, simple project and version control management. Over the time, quite a few of our clients have benefited from this setup as it can create instant project infrastructure.

But what is the cost of having these machines here?

Servers: Old HP desktop workstations from 2003. By the time they were state-of-the art workstations used by developers working on virtual machines. Now that everybody uses laptops, we set some of these machines up in our server room and have had immense benefit from them in the last 18 months or so.

2.6GHz XEON processor, 1GB ram, 2 scsi disks, mirrored raid. Two machines: One "production" server, one passive failover running rsync backup every 2 minutes. (and one shut down spare if the other machines fail).

## Power meter measurement

The other day I brought our power meter measurement tool from home. Here are the measurements for one machine:

- \
- Starting up: 137 Watts
  \
- Running 0.01-5% load: 100 Watts
  \
- Powered off: 26 Watts
  \
- (Danish voltage is 230 Volts)
  

With a cost of power in Denmark at 1.60 Danish Crowns (ex. vat) and an assumption of two machines running 24-7 this will give a cost of 1.400 Danish Crowns (DKK) per machine per year.

Let's assume that cooling will use 200W to remove the heat from 100W. **Total cost including cooling is thus 4.200DKK per machine per year.** There is also of course the cost of the shared components in the server room: Firewalls, switches, surveillance machine and perhaps routers for the internet connection. In this calculation I'm not including these -- that depends entirely on the number of machines that actually shares the infrastructure.

Two things that really surprised me: the power consumption of these old machines are actually pretty low. Also, that a powered down machine actually consumes 26W in standby power. One lesson I will remember is to pull the power cord on machines powered down. An easy way to be more environmentally correct.

Some questions I still have:

Are the assumtions of cooling effect actually valid? What kind of investment should be made to bring power consumtion further down (we still need multiple machines for a redundant fail-over setup)?
