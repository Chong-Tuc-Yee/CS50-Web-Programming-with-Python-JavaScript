document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // Extract info when user submit form
  document.querySelector('#compose-form').addEventListener('submit', send_newmail);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#content-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function view_content(id) {

  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {

    console.log(email);
    // Show view for email content and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#content-view').style.display = 'block';

    // Get div by ID from HTML page and display content
    document.querySelector('#content-view').innerHTML = `
      <h6><strong>From:</strong> ${email.sender}</h6>
      <h6><strong>To:</strong> ${email.recipients}</h6>
      <h6><strong>Subject:</strong> ${email.subject}</h6>
      <h6><strong>Timestamp:</strong> ${email.timestamp}</h6>
      <button class="btn btn-sm btn-outline-primary" id="replybtn"></button>
      <button class="btn btn-sm btn-outline-primary" id="archivebtn"></button>

      <hr>

      <p>${email.body}</p>
    `;

    // Change email read status
    if(!email.read){
      fetch(`/emails/${email.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            read: true
        })
      })
    };

    // Enable function for archive and unarchive email
    let archive = document.querySelector('#archivebtn');
    archive.innerHTML = email.archived ? 'Unarchive': 'Archive';
    // Change email archive status
    archive.addEventListener('click', function() {
      fetch(`/emails/${email.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: !email.archived
        })
      })
      // Load archive mailbox after operation
      .then(() => load_mailbox('archive'))
    });

    // Enable function for archive and unarchive email
    let reply = document.querySelector('#replybtn');
    reply.innerHTML = 'Reply';
    // Change email archive status
    reply.addEventListener('click', function() {

      compose_email();
      document.querySelector('#compose-recipients').value = email.sender;
      let subject = email.subject;
      // Format: string.split(separator, maxsplit). Check if Re: already exists in string and overwrite message.
      if(subject.split(' ',1)[0] != "Re:"){
        subject = "Re: " + email.subject;
      };
      document.querySelector('#compose-subject').value = subject;
      document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} wrote: ${email.body}`;
    });

  });
}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#content-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // JS get request to load corresponding page that user have chosen
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    // Loop through all the emails and create a div for each of them
    emails.forEach(email => {

      console.log(email);

      let show_email = document.createElement('div');
      // Provide class name for styling div
      show_email.className = 'list-group-item';
      // Display the sender, subject and timestamp from dictionary
      show_email.innerHTML = `
        <h6>Sender: ${email.sender}</h6>
        <h5>Subject: ${email.subject}</h5>
        <p>${email.timestamp}<p>
      `;
      // Display different background color for each individual email if read/not read
      show_email.className = email.read ? 'reademail': 'unreademail';
      // Need to add function() or will just direct show email content
      show_email.addEventListener('click', function() {
        view_content(email.id);
      });
      // Alternative: document.getElementById('emails.view').appendChild(show_email);
      document.querySelector('#emails-view').append(show_email);
    });
  });
}

function send_newmail(event) {
  // If event not handled prevent default action from taken as usual ie. form from submitting. Else form submits to itself and message flashes only a sec at output
  // Or we can add attribute onsubmit=False at form tag since type submit.
  event.preventDefault();

  const recipients = document.querySelector('#compose-recipients').value;
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value;

  // Sending HTTP POST request using JavaScript: fetch based on JS promises
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      console.log(result);
      // Load user's sent emailbox if sent successfully
      load_mailbox('sent');
  });
}
