# ICT171 Cloud Server Project

This project demonstrates the deployment of a web server on an AWS EC2 instance using Amazon Linux. It involves launching a virtual server, connecting via SSH, installing and configuring the Apache HTTP server, and verifying successful web hosting.

## 📁 GitHub Repository

[https://github.com/NEELLACHWANI/ICT171](https://github.com/NEELLACHWANI/ICT171)

## 🌐 Live Server

[http://3.27.234.91/](http://3.27.234.91/)

## 🚀 EC2 Instance Setup

- Instance launched with a key pair for SSH access.
- Apache installed using:

  ```bash
  sudo yum install httpd -y
  ```

- Apache service started and enabled.
- Custom message edited in `/var/www/html/index.html`.
- Port 80 configured for HTTP access in EC2 Security Group.

## 🔐 SSH Connection

SSH into the EC2 instance using the command:

```bash
ssh -i "connectKey.pem" ec2-user@ec2-3-27-234-91.ap-southeast-2.compute.amazonaws.com
```

This uses key-based authentication for secure access.

## 🎩 Demo Video

To embed a video in GitHub (if supported):

<video width="720" controls>
  <source src="demoVideo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
## 📽️ Demo Video

[▶️ Watch Demo Video](./demoVideo.mp4)


---
[📄 View Report (PDF)](./report.pdf)


## ✅ Output

- Successful setup and configuration of a web server.
- Public IP accessible showing the message:

  ```
  ICT171 Server is ON!
  Greetings from server (Neel)
  ```

This confirms that the server is up and running correctly on AWS EC2.

---

## 🗓️ Submission Details

**Student Name: Neel Kamlesh Lachwani**  
**Student ID: 35071098**  
**Date of Submission: 05 June 2025**
