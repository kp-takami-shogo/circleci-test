<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.css">
  <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>

  <link rel="stylesheet" href="style.css">
  <script src="main.js"></script>

  <title>CircleCI Demo</title>

</head>

<body>

<div class="container">

  <h1 class="title">CircleCI Demo</h1>

  <div class="field name-field">
    <label class="label">Name</label>
    <div class="control">
      <input class="input" type="text" placeholder="Text input" value="CircleCI">
    </div>
  </div>

  <div class="field username-field">
    <label class="label">User Name</label>
    <div class="control has-icons-left has-icons-right">
      <input class="input is-success" type="text" placeholder="Text input" value="CircleCI">
      <span class="icon is-small is-left">
      <i class="fas fa-user"></i>
    </span>
      <span class="icon is-small is-right">
      <i class="fas fa-check"></i>
    </span>
    </div>
    <p class="help is-success">This username is available</p>
  </div>

  <div class="field email-field">
    <label class="label">Email</label>
    <div class="control has-icons-left has-icons-right">
      <input class="input is-danger" type="email" placeholder="Email input" value="circleci@">
      <span class="icon is-small is-left">
      <i class="fas fa-envelope"></i>
    </span>
      <span class="icon is-small is-right">
      <i class="fas fa-exclamation-triangle"></i>
    </span>
    </div>
    <p class="help is-danger">This email is invalid</p>
  </div>

  <div class="field subject-field">
    <label class="label">Subject</label>
    <div class="control">
      <div class="select">
        <select>
          <option value="CircleCI" selected>CircleCI</option>
          <option value="Demo">Demo</option>
          <option value="KP">KP</option>
        </select>
      </div>
    </div>
  </div>

  <div class="field message-field">
    <label class="label">Message</label>
    <div class="control">
      <textarea class="textarea" placeholder="Textarea">CircleCI Demo</textarea>
    </div>
  </div>

  <div class="field terms-conditions-field">
    <div class="control">
      <label class="checkbox">
        <input type="checkbox">
        I agree to the <a href="#">terms and conditions</a>
      </label>
    </div>
  </div>

  <div class="field question-field">
    <div class="control">
      <label class="radio">
        <input type="radio" name="question">
        Yes
      </label>
      <label class="radio">
        <input type="radio" name="question" checked>
        No
      </label>
    </div>
  </div>

  <div class="field is-grouped submit-cancel-buttons">
    <div class="control">
      <button class="button is-link">Submit</button>
    </div>
    <div class="control">
      <button class="button is-text">Cancel</button>
    </div>
  </div>

</div>

</body>

</html>
