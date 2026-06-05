---
layout: page
title: Contact
permalink: /contact
comments: false
---

<div class="row mt-4">
    <!-- Contact Info Card -->
    <div class="col-md-5 mb-4">
        <div class="card bg-light border-0 shadow-sm p-4">
            <h4 class="font-weight-bold mb-3 text-dark">Get in Touch</h4>
            <p class="text-muted">Feel free to reach out for research collaborations, project discussions, or inquiries regarding my work in multimodal AI and robotics.</p>
            
            <hr class="my-3">
            
            <div class="contact-details">
                <div class="d-flex align-items-center mb-3">
                    <span class="mr-3 text-primary"><i class="fa fa-envelope fa-lg"></i></span>
                    <div>
                        <strong class="d-block text-dark">Email</strong>
                        <a href="mailto:km.jin0507@gmail.com" class="text-secondary">km.jin0507@gmail.com</a>
                    </div>
                </div>

                <div class="d-flex align-items-center mb-3">
                    <span class="mr-3 text-success"><i class="fa fa-map-marker fa-lg"></i></span>
                    <div>
                        <strong class="d-block text-dark">Affiliation</strong>
                        <span class="text-secondary">Advanced Robotics Lab, LG Electronics<br>Seoul, Republic of Korea</span>
                    </div>
                </div>

                <div class="d-flex align-items-center">
                    <span class="mr-3 text-info"><i class="fa fa-graduation-cap fa-lg"></i></span>
                    <div>
                        <strong class="d-block text-dark">Academic Scholar</strong>
                        <a href="https://scholar.google.com/citations?user=-d9eXb4AAAAJ&hl=en" target="_blank" class="text-secondary">Google Scholar Profile</a>
                    </div>
                </div>
            </div>

            <hr class="my-3">

            <div class="social-links mt-2">
                <a href="https://github.com/KyungMinJin" target="_blank" class="btn btn-outline-dark btn-sm mr-2">
                    <i class="fa fa-github"></i> GitHub
                </a>
                <a href="https://www.linkedin.com/in/경민-%E2%80%8D진-34594b1b7/" target="_blank" class="btn btn-outline-primary btn-sm">
                    <i class="fa fa-linkedin"></i> LinkedIn
                </a>
            </div>
        </div>
    </div>

    <!-- Contact Form Container -->
    <div class="col-md-7 mb-4">
        <div class="card border p-4 shadow-sm">
            <h4 class="font-weight-bold mb-4 text-dark">Send a Message</h4>
            
            <!-- Note: Replace "your-form-id" with your actual Formspree form ID (from https://formspree.io/) to make the form functional. -->
            <form action="https://formspree.io/f/mlgkdpnr" method="POST" id="contact-form">
                <div class="form-row">
                    <div class="form-group col-md-6">
                        <label for="name" class="text-dark font-weight-bold">Name</label>
                        <input type="text" class="form-control" id="name" name="name" placeholder="Your Name" required>
                    </div>
                    <div class="form-group col-md-6">
                        <label for="email" class="text-dark font-weight-bold">Email</label>
                        <input type="email" class="form-control" id="email" name="_replyto" placeholder="Your Email" required>
                    </div>
                </div>
                <div class="form-group">
                    <label for="subject" class="text-dark font-weight-bold">Subject</label>
                    <input type="text" class="form-control" id="subject" name="subject" placeholder="Subject" required>
                </div>
                <div class="form-group">
                    <label for="message" class="text-dark font-weight-bold">Message</label>
                    <textarea class="form-control" id="message" name="message" rows="5" placeholder="Write your message here..." required></textarea>
                </div>
                <button type="submit" class="btn btn-primary btn-block text-uppercase font-weight-bold">Send Message</button>
            </form>
        </div>
    </div>
</div>
