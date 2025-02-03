from flask import Flask, render_template, request, jsonify
import random 

app = Flask(__name__)


questions = [
    {
        "question": "¿Qué significa NVMe?",
        "options": ["Non-Volatile Memory Express", "Network Virtual Machine", "New Virtual Memory Engine"],
        "answer": "Non-Volatile Memory Express"
    },
    {
        "question": "¿Qué significa CPU?",
        "options": ["Central Processing Unit", "Computer Processing Unit", "Central Power Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "¿Qué significa IoT?",
        "options": ["Internet of Things", "Internet of Technology", "Integrated Online Technology"],
        "answer": "Internet of Things"
    },
    {
        "question": "¿Qué significa SSD?",
        "options": ["Solid State Drive", "Super Speed Disk", "System Storage Device"],
        "answer": "Solid State Drive"
    },
    {
        "question": "¿Qué significa HDD?",
        "options": ["Hard Disk Drive", "High Density Disk", "Hybrid Digital Drive"],
        "answer": "Hard Disk Drive"
    },
    {
        "question": "¿Qué significa GPU?",
        "options": ["Graphics Processing Unit", "General Processing Unit", "Global Power Unit"],
        "answer": "Graphics Processing Unit"
    },
    {
        "question": "¿Qué significa RAM?",
        "options": ["Random Access Memory", "Read-Only Memory", "Rapid Access Module"],
        "answer": "Random Access Memory"
    },
    {
        "question": "¿Qué significa ROM?",
        "options": ["Read-Only Memory", "Random Access Memory", "Rapid Operation Module"],
        "answer": "Read-Only Memory"
    },
    {
        "question": "¿Qué significa USB?",
        "options": ["Universal Serial Bus", "Ultra Speed Bus", "Unified System Bus"],
        "answer": "Universal Serial Bus"
    },
    {
        "question": "¿Qué significa LAN?",
        "options": ["Local Area Network", "Long Area Network", "Linked Access Network"],
        "answer": "Local Area Network"
    },
    {
        "question": "¿Qué significa WAN?",
        "options": ["Wide Area Network", "Wireless Area Network", "Web Access Network"],
        "answer": "Wide Area Network"
    },
    {
        "question": "¿Qué significa VPN?",
        "options": ["Virtual Private Network", "Virtual Public Network", "Verified Private Network"],
        "answer": "Virtual Private Network"
    },
    {
        "question": "¿Qué significa API?",
        "options": ["Application Programming Interface", "Advanced Programming Interface", "Automated Program Integration"],
        "answer": "Application Programming Interface"
    },
    {
        "question": "¿Qué significa HTML?",
        "options": ["HyperText Markup Language", "High-Level Text Language", "Hyperlink and Text Management Language"],
        "answer": "HyperText Markup Language"
    },
    {
        "question": "¿Qué significa CSS?",
        "options": ["Cascading Style Sheets", "Computer Style Sheets", "Creative Style System"],
        "answer": "Cascading Style Sheets"
    },
    {
        "question": "¿Qué significa JS?",
        "options": ["JavaScript", "Java Syntax", "Just Script"],
        "answer": "JavaScript"
    },
    {
        "question": "¿Qué significa SQL?",
        "options": ["Structured Query Language", "Simple Query Language", "System Query Logic"],
        "answer": "Structured Query Language"
    },
    {
        "question": "¿Qué significa AI?",
        "options": ["Artificial Intelligence", "Automated Intelligence", "Advanced Interface"],
        "answer": "Artificial Intelligence"
    },
    {
        "question": "¿Qué significa ML?",
        "options": ["Machine Learning", "Mainframe Logic", "Memory Learning"],
        "answer": "Machine Learning"
    },
    {
        "question": "¿Qué significa DL?",
        "options": ["Deep Learning", "Data Logic", "Digital Learning"],
        "answer": "Deep Learning"
    },
    {
        "question": "¿Qué significa VR?",
        "options": ["Virtual Reality", "Visual Rendering", "Voice Recognition"],
        "answer": "Virtual Reality"
    },
    {
        "question": "¿Qué significa AR?",
        "options": ["Augmented Reality", "Advanced Rendering", "Audio Recognition"],
        "answer": "Augmented Reality"
    },
    {
        "question": "¿Qué significa MR?",
        "options": ["Mixed Reality", "Memory Rendering", "Media Recognition"],
        "answer": "Mixed Reality"
    },
    {
        "question": "¿Qué significa BIOS?",
        "options": ["Basic Input/Output System", "Binary Input/Output System", "Boot Initialization System"],
        "answer": "Basic Input/Output System"
    },
    {
        "question": "¿Qué significa UEFI?",
        "options": ["Unified Extensible Firmware Interface", "Universal Embedded Firmware Interface", "Unified External Firmware Integration"],
        "answer": "Unified Extensible Firmware Interface"
    },
    {
        "question": "¿Qué significa DNS?",
        "options": ["Domain Name System", "Dynamic Network System", "Data Naming Service"],
        "answer": "Domain Name System"
    },
    {
        "question": "¿Qué significa DHCP?",
        "options": ["Dynamic Host Configuration Protocol", "Domain Host Configuration Protocol", "Data Handling Control Protocol"],
        "answer": "Dynamic Host Configuration Protocol"
    },
    {
        "question": "¿Qué significa IP?",
        "options": ["Internet Protocol", "Internal Protocol", "Integrated Platform"],
        "answer": "Internet Protocol"
    },
    {
        "question": "¿Qué significa TCP?",
        "options": ["Transmission Control Protocol", "Transfer Communication Protocol", "Traffic Control Protocol"],
        "answer": "Transmission Control Protocol"
    },
    {
        "question": "¿Qué significa HTTP?",
        "options": ["HyperText Transfer Protocol", "High-Level Transfer Protocol", "Hyperlink Transfer Process"],
        "answer": "HyperText Transfer Protocol"
    },
    {
        "question": "¿Qué significa HTTPS?",
        "options": ["HyperText Transfer Protocol Secure", "High-Level Transfer Protocol Secure", "Hyperlink Transfer Process Secure"],
        "answer": "HyperText Transfer Protocol Secure"
    },
    {
        "question": "¿Qué significa FTP?",
        "options": ["File Transfer Protocol", "Fast Transfer Protocol", "Flexible Transfer Process"],
        "answer": "File Transfer Protocol"
    },
    {
        "question": "¿Qué significa SSH?",
        "options": ["Secure Shell", "System Secure Hub", "Server Security Handler"],
        "answer": "Secure Shell"
    },
    {
        "question": "¿Qué significa SSL?",
        "options": ["Secure Sockets Layer", "System Security Layer", "Server Security Logic"],
        "answer": "Secure Sockets Layer"
    },
    {
        "question": "¿Qué significa TLS?",
        "options": ["Transport Layer Security", "Traffic Layer Security", "Transfer Logic System"],
        "answer": "Transport Layer Security"
    },
    {
        "question": "¿Qué significa CDN?",
        "options": ["Content Delivery Network", "Centralized Data Network", "Cloud Distribution Node"],
        "answer": "Content Delivery Network"
    },
    {
        "question": "¿Qué significa CMS?",
        "options": ["Content Management System", "Centralized Management System", "Cloud Management Service"],
        "answer": "Content Management System"
    },
    {
        "question": "¿Qué significa ERP?",
        "options": ["Enterprise Resource Planning", "Efficient Resource Planning", "Extended Resource Platform"],
        "answer": "Enterprise Resource Planning"
    },
    {
        "question": "¿Qué significa CRM?",
        "options": ["Customer Relationship Management", "Centralized Resource Management", "Client Resource Module"],
        "answer": "Customer Relationship Management"
    },
    {
        "question": "¿Qué significa SaaS?",
        "options": ["Software as a Service", "System as a Service", "Storage as a Service"],
        "answer": "Software as a Service"
    },
    {
        "question": "¿Qué significa PaaS?",
        "options": ["Platform as a Service", "Processing as a Service", "Protocol as a Service"],
        "answer": "Platform as a Service"
    },
    {
        "question": "¿Qué significa IaaS?",
        "options": ["Infrastructure as a Service", "Integration as a Service", "Interface as a Service"],
        "answer": "Infrastructure as a Service"
    },
    {
        "question": "¿Qué significa REST?",
        "options": ["Representational State Transfer", "Remote Execution System Transfer", "Resource Exchange System Transfer"],
        "answer": "Representational State Transfer"
    },
    {
        "question": "¿Qué significa SOAP?",
        "options": ["Simple Object Access Protocol", "System Object Access Protocol", "Secure Object Access Protocol"],
        "answer": "Simple Object Access Protocol"
    },
    {
        "question": "¿Qué significa JSON?",
        "options": ["JavaScript Object Notation", "Java Standard Object Notation", "JavaScript Oriented Network"],
        "answer": "JavaScript Object Notation"
    },
    {
        "question": "¿Qué significa XML?",
        "options": ["eXtensible Markup Language", "Extended Markup Language", "Exchangeable Markup Language"],
        "answer": "eXtensible Markup Language"
    },
    {
        "question": "¿Qué significa GUI?",
        "options": ["Graphical User Interface", "General User Interface", "Global User Integration"],
        "answer": "Graphical User Interface"
    },
    {
        "question": "¿Qué significa CLI?",
        "options": ["Command Line Interface", "Centralized Logic Interface", "Control Line Integration"],
        "answer": "Command Line Interface"
    }
]


def shuffle_options():
    for question in questions:
        random.shuffle(question["options"]) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_questions')
def get_questions():
    shuffle_options()
    return jsonify(questions)

if __name__ == '__main__':
    app.run()